from pydantic import BaseModel, EmailStr
class CandidateEmailRequest(BaseModel):
    name: str
    email: EmailStr
    position:str
    status: str