import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

from backend.schemas import CandidateEmailRequest
from backend.email_templates import selection_template, rejection_template

app = FastAPI(title="HR Email Tool")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(to_email: str, subject: str, body: str):
    """Utility function to handle the SMTP connection and sending."""
    if not all([SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD]):
        raise HTTPException(
            status_code=500, 
            detail="Email configuration is missing in server environment variables."
        )

    try:
        msg = EmailMessage()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
    except Exception as e:
        print(f"SMTP Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

@app.post("/preview")
def preview_email(data: CandidateEmailRequest):
    """Generates a preview of the email without sending it."""
    template = selection_template if data.status.lower() == "selected" else rejection_template

    try:
        email_body = template.format(
            name=data.name,
            position=data.position
        )
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Template formatting error: Missing {e}")

    return {
        "to": data.email,
        "subject": f"Regarding your application for {data.position}",
        "body": email_body
    }

@app.post("/send")
def send_candidate_email(data: CandidateEmailRequest):
    """Formats the template and sends the actual email."""
    template = selection_template if data.status.lower() == "selected" else rejection_template

    email_body = template.format(
        name=data.name,
        position=data.position
    )

    send_email(
        to_email=data.email,
        subject=f"Regarding your application for {data.position}",
        body=email_body
    )

    return {"status": "success", "message": f"Email successfully sent to {data.email}"}