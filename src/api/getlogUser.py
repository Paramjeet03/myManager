from src.CRUD.User_crud import get_user_id,getlog_user
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import user

router=APIRouter()

@router.get("/")
def getloguser(current_user:dict=user):
    try:
        id=get_user_id(name=current_user['username'])
        return getlog_user(id=id)
    except HTTPException as e:
        raise e