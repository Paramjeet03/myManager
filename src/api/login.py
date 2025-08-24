from fastapi import APIRouter
from src.pydantic_schema.User_pydantic import UserLogin
from src.Auth.Authentication import user_login


router = APIRouter()

@router.post("/")
def login(login_data:UserLogin):
    token = user_login(login_data)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
