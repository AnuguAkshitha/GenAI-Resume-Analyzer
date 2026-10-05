# GenAI-Powered Resume Analyzer and Intelligent Job Matching System

A student-friendly Generative AI project that analyzes a PDF resume against a job description and produces an ATS-style match estimate, skill gaps, improvement suggestions, and interview questions.

## Features
- PDF resume upload
- Resume text extraction using PyPDF
- Job-description input
- Gemini GenAI analysis
- ATS-style match score
- Matching and missing skills
- Resume strengths
- Improvement suggestions
- Personalized interview questions
- AI-generated professional summary
- API key stored in `.env`

## Technology Stack
- Python
- Flask
- HTML/CSS
- Google GenAI Python SDK
- Gemini model
- PyPDF
- JSON
- SQLite can be added later for storing analysis history

## Project Structure

genai_resume_analyzer/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── DOCUMENTATION.md
├── templates/
│   └── index.html
└── static/
    └── style.css

## Setup

1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create a virtual environment:

   python -m venv venv

4. Activate it.

Windows:
   venv\Scripts\activate

macOS/Linux:
   source venv/bin/activate

5. Install packages:

   pip install -r requirements.txt

6. Copy `.env.example` to `.env`.
7. Put your Gemini API key in `.env`.
8. Run:

   python app.py

9. Open:
   http://127.0.0.1:5000

## Important
Never upload your `.env` file to GitHub. The `.gitignore` file is already configured to exclude it.

## How the AI part works
The backend extracts resume text, combines it with the job description, and sends a structured prompt to Gemini. The model is asked to return JSON so the Flask application can display the result in separate dashboard sections.

## Future Enhancements
- Login and user profiles
- SQLite analysis history
- DOCX resume support
- Keyword visualization
- Resume section scoring
- RAG using a personal knowledge base
- Export analysis as PDF
- Deployment using a cloud platform
