from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import os
from dotenv import load_dotenv
import logging
import json
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('hr_assistant.log')
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
if not load_dotenv():
    logger.warning(".env file not found or couldn't be loaded")

# Validate required environment variables
required_vars = [
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_KEY",
    "AZURE_COGNITIVE_ENDPOINT",
    "AZURE_COGNITIVE_KEY"
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

# Define request models
class JobDescriptionRequest(BaseModel):
    job_description: str
    
    class Config:
        min_length = 10
        max_length = 5000

class ResumeScreenRequest(BaseModel):
    resume: str
    job_description: str
    
    class Config:
        min_length = 10
        max_length = 5000

class JobParametersRequest(BaseModel):
    parameters: Dict[str, Any]

class EmployeeDataRequest(BaseModel):
    employee_data: Dict[str, Any]

class HRDocumentRequest(BaseModel):
    template_type: str
    employee_data: Dict[str, Any]

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files correctly
app.mount("/static", StaticFiles(directory="static/static"), name="static")

# Serve frontend index.html
@app.get("/")
async def serve_spa(request: Request):
    return FileResponse("static/index.html")

# Catch all routes for SPA
@app.get("/{full_path:path}")
async def serve_spa_paths(full_path: str):
    if os.path.exists(f"static/{full_path}"):
        return FileResponse(f"static/{full_path}")
    return FileResponse("static/index.html")

# Serve other static assets from root build directory
@app.get("/{filename:path}")
async def serve_static(filename: str):
    static_file = f"static/{filename}"
    if os.path.isfile(static_file):
        return FileResponse(static_file)
    return FileResponse("static/index.html")

# Azure OpenAI Configuration
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

# Azure Cognitive Services Configuration
text_analytics_endpoint = os.getenv("AZURE_COGNITIVE_ENDPOINT")
text_analytics_key = os.getenv("AZURE_COGNITIVE_KEY")
text_analytics_client = TextAnalyticsClient(endpoint=text_analytics_endpoint, 
                                          credential=AzureKeyCredential(text_analytics_key))

class HRServices:
    @staticmethod
    def generate_interview_questions(job_description):
        logger.info("Generating interview questions")
        try:
            prompt = f"Generate 10 technical screening interview questions based on this job description: {job_description}"
            response = openai.Completion.create(
                engine="gpt-35-turbo",
                prompt=prompt,
                max_tokens=1000
            )
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Error generating interview questions: {str(e)}")
            raise

    @staticmethod
    def screen_resume(resume_text, job_description):
        logger.info("Screening resume against job description")
        try:
            # Extract key phrases from both resume and job description
            resume_analysis = text_analytics_client.extract_key_phrases([resume_text])[0]
            job_analysis = text_analytics_client.extract_key_phrases([job_description])[0]
            
            # Compare skills and experience
            prompt = f"Compare the resume:\n{resume_text}\n\nWith the job description:\n{job_description}\n\nProvide a matching score and detailed analysis."
            response = openai.Completion.create(
                engine="gpt-35-turbo",
                prompt=prompt,
                max_tokens=500
            )
            return response.choices[0].text.strip()
        except Exception as e:
            logger.error(f"Error screening resume: {str(e)}")
            raise

    @staticmethod
    def generate_job_description(params):
        prompt = f"Generate a detailed job description based on these parameters: {json.dumps(params)}"
        response = openai.Completion.create(
            engine="gpt-35-turbo",
            prompt=prompt,
            max_tokens=800
        )
        return response.choices[0].text.strip()

    @staticmethod
    def suggest_internal_mobility(employee_data):
        prompt = f"Suggest potential internal positions based on this employee's skills and experience: {json.dumps(employee_data)}"
        response = openai.Completion.create(
            engine="gpt-35-turbo",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    @staticmethod
    def generate_hr_document(template_type, employee_data):
        prompt = f"Generate a {template_type} using this employee data: {json.dumps(employee_data)}"
        response = openai.Completion.create(
            engine="gpt-35-turbo",
            prompt=prompt,
            max_tokens=1000
        )
        return response.choices[0].text.strip()

@app.post("/api/interview-questions")
async def generate_interview_questions(request: JobDescriptionRequest):
    logger.info("Received request for interview questions")
    try:
        questions = HRServices.generate_interview_questions(request.job_description)
        return {"questions": questions}
    except Exception as e:
        logger.error(f"Error in interview questions endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/screen-resume")
async def screen_resume(request: ResumeScreenRequest):
    logger.info("Received request for resume screening")
    try:
        analysis = HRServices.screen_resume(request.resume, request.job_description)
        return {"analysis": analysis}
    except Exception as e:
        logger.error(f"Error in resume screening endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/job-description")
async def generate_job_description(request: JobParametersRequest):
    description = HRServices.generate_job_description(request.parameters)
    return {"job_description": description}

@app.post("/api/internal-mobility")
async def suggest_internal_mobility(request: EmployeeDataRequest):
    suggestions = HRServices.suggest_internal_mobility(request.employee_data)
    return {"suggestions": suggestions}

@app.post("/api/hr-document")
async def generate_hr_document(request: HRDocumentRequest):
    document = HRServices.generate_hr_document(request.template_type, request.employee_data)
    return {"document": document}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error handler: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error occurred"}
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - {response.status_code} - {duration:.2f}s")
    return response

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv('PORT', 8080))
    debug = os.getenv('FLASK_ENV', 'production') == 'development'
    uvicorn.run("backend:app", host="0.0.0.0", port=port, reload=debug)