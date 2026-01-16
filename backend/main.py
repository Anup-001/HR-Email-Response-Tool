from FastAPI import FastAPI, HTTPException
from FastAPI.middleware.cors import CORSMiddleware
from schemas import CandidateEmailRequest
from email_templates import selection_template, rejection_template
import smtplib
from email.message import EmailMessage

app=FastAPI(title="HR Email Tool")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
SMTP_SERVER=''
SMTP_PORT=587
SENDER_EMAIL=''
SENDER_PASSWORD=''

def send_email(to_email: str,subject: str,body:str):
    try:
        msg=EmailMessage()
        msg['From']=SENDER_EMAIL
        msg['To']=to_email
        msg['Subject']=subject
        msg.setcontent(body)
        
        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.send_message(msg)
            