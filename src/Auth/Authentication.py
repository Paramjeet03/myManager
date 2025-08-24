from fastapi import HTTPException,status
from src.pydantic_schema.User_pydantic import UserLogin
from src.Auth.Hashing_token import verify_pass,create_token
from src.CRUD.User_crud import get_user

def user_login(login:UserLogin):
    data=get_user(login)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credential")
    elif not verify_pass(login.password,data.pass_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Password")
    else:
        return create_token(data={"username":data.name,"role":data.role})

