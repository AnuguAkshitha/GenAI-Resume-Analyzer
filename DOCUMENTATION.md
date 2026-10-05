# PROJECT DOCUMENTATION

## 1. Title
GenAI-Powered Resume Analyzer and Intelligent Job Matching System

## 2. Abstract
The GenAI-Powered Resume Analyzer and Intelligent Job Matching System is a web-based application designed to help students and job seekers understand how well their resumes align with a particular job description. The system accepts a PDF resume and a job description as input. It extracts the resume text and uses a Generative AI model to compare the candidate's skills, projects, education and experience with the requirements in the job description.

The application produces an ATS-style match score, matching skills, missing skills, strengths, improvement suggestions, interview questions and an improved professional summary. The system is intended as a career-support tool and its score is an estimate rather than a guarantee of the result from any employer's Applicant Tracking System.

## 3. Problem Statement
Students often submit the same resume to different companies without understanding whether it matches the specific job description. They may miss important keywords, skills or requirements. Manual comparison is time-consuming and may not provide personalized interview preparation.

## 4. Proposed Solution
The proposed system uses Generative AI to analyze the resume and job description together. It provides personalized feedback and identifies skill gaps. It also generates interview questions from the candidate's actual resume and the target role.

## 5. Objectives
1. Extract text from PDF resumes.
2. Compare resume content with job requirements.
3. Generate an ATS-style match estimate.
4. Identify matching and missing skills.
5. Provide actionable resume improvement suggestions.
6. Generate role-specific interview questions.
7. Generate a truthful professional summary.
8. Provide a simple web interface for students.

## 6. Scope
The system is suitable for:
- College students
- Freshers
- Internship applicants
- Entry-level job seekers
- Placement preparation

The system does not replace a company's actual ATS or recruiter.

## 7. Functional Requirements

### FR1: Resume Upload
The user can upload a PDF resume.

### FR2: Text Extraction
The system extracts text from the PDF using PyPDF.

### FR3: Job Description
The user enters or pastes a job description.

### FR4: AI Analysis
The system sends the extracted resume and job description to the GenAI model.

### FR5: Result Generation
The model returns:
- Match score
- Summary
- Matching skills
- Missing skills
- Strengths
- Improvements
- Interview questions
- Improved summary

### FR6: Result Display
The Flask web application displays the generated information in a readable dashboard.

## 8. Non-Functional Requirements
- Simple and responsive interface
- Secure API-key handling
- Reasonable response time
- Easy maintenance
- Clear error messages
- No fabricated candidate information in the AI prompt instructions

## 9. System Architecture

User
  |
  v
Web Browser
  |
  v
Flask Application
  |
  +--> PDF Text Extraction (PyPDF)
  |
  +--> Prompt Construction
  |
  v
Gemini GenAI API
  |
  v
Structured JSON Response
  |
  v
Flask Result Dashboard

## 10. Modules

### Module 1: User Interface
Provides resume upload and job-description input.

### Module 2: PDF Processing
Reads each PDF page and extracts text.

### Module 3: GenAI Processing
Creates a recruiter-style prompt and sends it to Gemini.

### Module 4: Result Processing
Parses the AI JSON response.

### Module 5: Dashboard
Displays the analysis in separate sections.

## 11. Algorithm

Step 1: Start application.
Step 2: User uploads PDF resume.
Step 3: Validate file type.
Step 4: Extract text from PDF.
Step 5: User enters job description.
Step 6: Validate both inputs.
Step 7: Build GenAI prompt.
Step 8: Send prompt to Gemini.
Step 9: Receive structured JSON response.
Step 10: Parse response.
Step 11: Display score, skills, suggestions and questions.
Step 12: End.

## 12. GenAI Prompt Design
The prompt gives the model a specific role as a technical recruiter and requires valid JSON. It also explicitly tells the model not to invent experience or qualifications. Structured output makes the response easier for the Flask application to process.

## 13. Database
The first version does not require a database because the analysis is generated per request. SQLite can be added as a future module to store:
- User ID
- Resume filename
- Job title
- Match score
- Analysis date
- Saved suggestions

## 14. Security
- API key is stored in `.env`.
- `.env` is excluded through `.gitignore`.
- Uploaded files are not permanently stored by this version.
- User should avoid sending highly sensitive personal information to external AI services.

## 15. Advantages
- Saves resume-review time
- Personalized feedback
- Useful for placement preparation
- Generates interview questions
- Easy to use
- Demonstrates practical GenAI integration

## 16. Limitations
- AI-generated score is only an estimate.
- PDF extraction may fail for scanned/image-only PDFs.
- AI output can occasionally be inaccurate.
- The quality of feedback depends on the resume and job description.
- Requires internet access and a valid API key.

## 17. Future Enhancements
1. OCR for scanned resumes.
2. DOCX support.
3. User login.
4. SQLite/MySQL history.
5. Resume improvement editor.
6. Downloadable PDF report.
7. RAG-based interview assistant.
8. Job recommendation module.
9. Skill-learning recommendations.
10. Deployment as a cloud web application.

## 18. Testing

### Test Case 1
Input: Valid PDF + valid job description
Expected: Analysis dashboard is displayed.

### Test Case 2
Input: No resume
Expected: "Please upload a PDF resume."

### Test Case 3
Input: JPG resume
Expected: "Only PDF files are supported."

### Test Case 4
Input: Resume + empty job description
Expected: "Please enter a job description."

### Test Case 5
Input: Image-only/scanned PDF
Expected: Text extraction warning.

## 19. Conclusion
The GenAI-Powered Resume Analyzer demonstrates how Generative AI can be integrated into a practical web application. It combines document processing, prompt engineering, API integration and web development to provide personalized career assistance. The project is especially useful for students preparing for internships and placement interviews.

## 20. Viva Questions

Q1. What is Generative AI?
A: Generative AI creates new content such as text, code, images or summaries based on user input and learned patterns.

Q2. Why did you use GenAI?
A: Traditional keyword matching can identify words, but GenAI can understand context and provide personalized suggestions and interview questions.

Q3. Why Flask?
A: Flask is a lightweight Python web framework that is simple to develop and suitable for small web applications.

Q4. How is the resume read?
A: The application uses PyPDF to extract text from PDF pages.

Q5. How does the AI generate the match score?
A: The prompt asks Gemini to compare the resume and job description and return an estimated score from 0 to 100.

Q6. Is this the actual ATS score?
A: No. It is an AI-generated estimate. Different companies use different ATS systems and scoring methods.

Q7. What is prompt engineering?
A: Prompt engineering is the process of designing clear instructions and constraints so an AI model produces useful and consistent results.

Q8. Why JSON?
A: JSON provides structured output that Python can parse and display in different UI sections.

Q9. Where is the API key stored?
A: In the `.env` environment file, not directly in the source code.

Q10. What can you add in future?
A: RAG, OCR, database history, DOCX support, report export and job recommendations.
