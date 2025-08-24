from pydantic import BaseModel, EmailStr 
from src.Enum_modal.Enum import roleEnum
from typing import Optional



class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone :str
    role: roleEnum

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

   

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Update_user(BaseModel):
     email:EmailStr
     role:Optional[roleEnum] =None
     name:str = None




class Config:
    from_attributes = True