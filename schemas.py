from pydantic import BaseModel
from pydantic import EmailStr
from typing import List

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    
class TokenResponse(BaseModel):
    token: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

class TodoListResponse(BaseModel):
    data: List[TodoResponse]
    page: int
    limit: int
    total: int
    

