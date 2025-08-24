from src.CRUD.Admin_crud import delete_user_table
from fastapi import APIRouter,HTTPException,status
from src.pydantic_schema.User_pydantic import EmailStr
from src.Dependancy.dependancy import admin
from src.Config.Config import setting
router=APIRouter()

@router.delete("/")
def deletion(Email:EmailStr, current_user: dict = admin):
    try:
        if Email.lower().strip()==setting.SUPER_MAIL:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allow")
        master=current_user["username"]
        delete_user_table(user_email=Email,master=master)
        return {"message":"Deletion Done sucessfully"}
    except HTTPException as http:
        raise http