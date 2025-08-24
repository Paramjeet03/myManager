from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi import HTTPException,Depends
from src.Auth.Authorization import token_decode

def oauth2_scheme():
    return OAuth2PasswordBearer(tokenUrl="/login")


def admin_only(current_user: dict = Depends(token_decode)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="User not allowed")
    return current_user

def user_only(current_user:dict=Depends(token_decode)):
    if current_user["role"] == "admin":
        raise HTTPException(status_code=403, detail="Admins Not allowed")
    return current_user

def both_user(current_user:dict=Depends(token_decode)):
    if current_user["role"] != "admin":
        return current_user
    elif current_user["role"] == "admin":
        return current_user

admin=Depends(admin_only)
user=Depends(user_only)
both=Depends(both_user)