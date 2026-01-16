from pydantic import BaseModel, EmailStr
class CandidateEmailRequest(BaseModel):
    name: str
    email: EmailStr
    postition:str
    status: str