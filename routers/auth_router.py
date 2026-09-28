from fastapi import APIRouter, HTTPException
from schemas import UserRegister, TokenResponse
from crud import get_user_by_email, create_user
from auth import hash_password, create_access_token

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