from src.CRUD.Admin_crud import getlog_admin
from src.pydantic_schema.User_log_pydantic import getlog
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.post("/")
def getlogAdmin(id:getlog,current_user:dict = admin):
    try:
        return getlog_admin(log_id=id)
    except HTTPException as e:
        raise e