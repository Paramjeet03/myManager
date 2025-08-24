from src.CRUD.Admin_crud import assignTask
from src.pydantic_schema.task_pydantic import TaskCreate
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.post("/")
def assigntask(task:TaskCreate,current_user:dict = admin):
    if  not task.title.strip() or not task.description.strip() or not task.status.strip():
        raise HTTPException(status_code=400,detail="Empty string is not allowed")
    else:
        try:
            master=current_user["username"]
            assignTask(task=task,master=master)
            return {"message":"Done"}
        except HTTPException as e:
            raise e