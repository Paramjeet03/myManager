from fastapi import APIRouter
from src.CRUD.User_crud import getTask,get_user_id
from src.Dependancy.dependancy import user

router=APIRouter()

@router.get("/")
def get_Task(current_user:dict = user):
    id=get_user_id(name=current_user['username'])
    return getTask(user_id=id)

    