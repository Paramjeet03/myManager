from src.CRUD.Admin_crud import Update_user_table
from fastapi import APIRouter,HTTPException,status
from src.pydantic_schema.User_pydantic import Update_user
from src.Dependancy.dependancy import admin
from src.Config.Config import setting

router=APIRouter()

@router.put("/")
def updation(user:Update_user, current_user: dict = admin):
    try:
        if user.email.lower().strip()==setting.SUPER_MAIL:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allow")
        master=current_user["username"]
        Update_user_table(user=user,master=master)
        return {"message":"Updation Done sucessfully"}
    except HTTPException as http:
        raise http
