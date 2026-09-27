from pydantic import BaseModel
from pydantic import EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    
class TokenResponse(BaseModel):
    token: str