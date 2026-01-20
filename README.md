# 📧 HR Candidate Email Response Tool

A lightweight, full-stack web application designed to help HR teams streamline candidate communication. This tool allows users to input candidate details, select their status (Selected/Rejected), and send professional emails using predefined templates.

## 🚀 Features
- **Automated Templates:** Dynamically generates emails using candidate names and job positions.
- **Instant Preview:** Real-time preview of the email content before sending.
- **Modern UI:** Responsive design built with Tailwind CSS.
- **Secure Backend:** FastAPI logic with environment variable protection for SMTP credentials.
- **Data Validation:** Strict type-checking using Pydantic to ensure valid email delivery.

---

## 📂 Project Structure
```text
root/
├── frontend/
│   └── index.html          # Web interface & JavaScript Fetch logic
├── backend/
│   ├── main.py             # FastAPI entry point & SMTP logic
│   ├── schemas.py          # Pydantic data models
│   └── email_templates.py  # Email string constants
├── .env                    # Private credentials (not to be shared)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

---

🛠️ Setup Instructions
1. Backend Setup (Python 3.8+)
Navigate to the backend directory and install dependencies:

Bash

pip install fastapi uvicorn pydantic[email] python-dotenv
2. Configure Email Settings
Create a .env file in the root directory and add your SMTP credentials:

Plaintext

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
Note: If using Gmail, you must generate an App Password in your Google Account security settings.

3. Run the Application
Start the FastAPI server:

Bash

uvicorn backend.main:app --reload
The backend will be running at http://127.0.0.1:8000.

4. Launch the Frontend
Simply open frontend/index.html in any modern web browser.

📖 How to Use
Enter the Candidate Name, Email, and the Position they applied for.

Select their application Status (Selected or Rejected).

Click Preview to review the generated text.

Click Send Email to deliver the message via the SMTP server.

🛡️ Technical Highlights
Frontend: HTML5, JavaScript (Async/Await Fetch), Tailwind CSS.

Backend: Python (FastAPI framework).

Security: CORS middleware enabled for local development; Sensitive data stored in .env.

Formatting: Used Python triple-quoted strings and .format() for clean template injection.