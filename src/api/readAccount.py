from fastapi import APIRouter,HTTPException,status
from src.Dependancy.dependancy import admin
from pydantic import EmailStr
from src.CRUD.Admin_crud import get_user
from src.Config.Config import setting

router = APIRouter()

@router.get("/")
def readAcount(Email:EmailStr,current_user:dict=admin):
    try:
        if Email.lower().strip()==setting.SUPER_MAIL:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allow")
        return get_user(user_email=Email)
    except HTTPException as e:
        raise e

    