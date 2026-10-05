import os
import json
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret")
ALLOWED_EXTENSIONS = {"pdf"}

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_pdf_text(file_storage):
    reader = PdfReader(file_storage)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).strip()


def analyze_with_gemini(resume_text, job_description):
    if not client:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    prompt = f"""
You are an expert technical recruiter and resume coach.

Analyze the candidate resume against the job description below.
Do not invent experience, skills, education, projects, or certifications.
Give a realistic ATS-style estimate, not a claim about any company's actual ATS.

Return ONLY valid JSON with exactly these keys:
{{
  "match_score": 0,
  "summary": "",
  "matching_skills": [],
  "missing_skills": [],
  "strengths": [],
  "improvements": [],
  "interview_questions": [],
  "improved_summary": ""
}}

Rules:
- match_score must be an integer from 0 to 100.
- matching_skills and missing_skills: concise skill names.
- strengths and improvements: 3 to 5 useful points.
- interview_questions: 5 to 8 questions based only on the resume and job description.
- improved_summary: 3 to 5 lines, professional and truthful.

RESUME:
{resume_text[:18000]}

JOB DESCRIPTION:
{job_description[:12000]}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    text = response.text.strip()
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    resume_name = None

    if request.method == "POST":
        resume = request.files.get("resume")
        job_description = request.form.get("job_description", "").strip()

        if not resume or not resume.filename:
            flash("Please upload a PDF resume.")
            return render_template("index.html")

        if not allowed_file(resume.filename):
            flash("Only PDF files are supported.")
            return render_template("index.html")

        if not job_description:
            flash("Please enter a job description.")
            return render_template("index.html")

        try:
            resume_name = secure_filename(resume.filename)
            resume_text = extract_pdf_text(resume)

            if len(resume_text) < 50:
                flash("Could not extract enough text from the PDF. Try a text-based PDF.")
                return render_template("index.html")

            result = analyze_with_gemini(resume_text, job_description)
        except json.JSONDecodeError:
            flash("The AI returned an unexpected format. Please try again.")
        except Exception as exc:
            flash(f"Analysis failed: {exc}")

    return render_template("index.html", result=result, resume_name=resume_name)


if __name__ == "__main__":
    app.run(debug=True)
