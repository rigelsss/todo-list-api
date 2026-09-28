from fastapi import APIRouter, HTTPException
from schemas import UserRegister, TokenResponse, UserLogin
from crud import get_user_by_email, create_user
from auth import hash_password, create_access_token, verify_password

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
def register(user: UserRegister):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User with this email already exists."
        )
    hashed_password = hash_password(user.password)
    new_user = create_user(user.name, user.email, hashed_password)
    access_token = create_access_token({"user_id": new_user[0]})
    
    return TokenResponse(token=access_token)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    existing_user = get_user_by_email(user.email)
    
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )
    password_hash = existing_user[3]
    
    if not verify_password(user.password, password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )
    
    access_token = create_access_token({"user_id": existing_user[0]})
    return TokenResponse(token=access_token)