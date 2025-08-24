from passlib.context import CryptContext
from src.Config.Config import setting
from src.pydantic_schema.User_pydantic import UserCreate
from datetime import datetime,timedelta,timezone
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
pwdContext=CryptContext(schemes=[setting.PWD_HASH_ALGO],deprecated="auto")

def hash_pass(plain_pwd : str):
    return pwdContext.hash(plain_pwd)

def verify_pass(plain_pwd:str,hash_pwd:str):
    return pwdContext.verify(plain_pwd,hash_pwd)

def create_token( data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)





