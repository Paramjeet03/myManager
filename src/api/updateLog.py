from src.CRUD.User_crud import updatelog
from src.pydantic_schema.User_log_pydantic import add_log
from fastapi import APIRouter,HTTPException,status
from src.Dependancy.dependancy import user

router=APIRouter()

@router.put("/")
def updateLogFunc(log:add_log,current_user:dict = user):
    try:
        return updatelog(log=log,name=current_user["username"])
    except HTTPException as e:
        raise e