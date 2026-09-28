from pydantic import BaseModel
from pydantic import EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    
class TokenResponse(BaseModel):
    token: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
