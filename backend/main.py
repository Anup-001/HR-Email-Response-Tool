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
            
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Failed to send email: {str(e)}")
    
@app.post("/preview")
def preview_email(data: CandidateEmailRequest):
    template = (
        selection_template if data.status == "selected" else rejection_template
    )

    email_body = template.format(
        name=data.name,
        position=data.position
    )

    return {
        "to": data.email,
        "subject": f"Regarding your application for {data.position}",
        "body": email_body
    }


@app.post("/send")
def send_candidate_email(data: CandidateEmailRequest):
    template = (
        selection_template if data.status == "selected" else rejection_template
    )

    email_body = template.format(
        name=data.name,
        position=data.position
    )

    send_email(
        to_email=data.email,
        subject=f"Regarding your application for {data.position}",
        body=email_body
    )

    return {"message": "Email sent successfully"}