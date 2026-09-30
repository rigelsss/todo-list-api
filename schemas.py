from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class UserRegister(BaseModel):
    name: str = Field(min_length=4, max_length=255)
    email: EmailStr
    password: str = Field(min_length=4)
    
    
class TokenResponse(BaseModel):
    token: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1)

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
    
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, min_length=1)
    is_completed: Optional[bool] = None
    

