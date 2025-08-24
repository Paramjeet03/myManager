from src.CRUD.Admin_crud import deleteTask
from fastapi import APIRouter,HTTPException
from src.pydantic_schema.task_pydantic import TaskOut
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.delete("/")
def deletion(out:TaskOut,current_user : dict = admin):
    try:
        return deleteTask(out=out)
    except HTTPException as h:
        raise h

    