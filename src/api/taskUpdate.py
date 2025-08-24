from src.Dependancy.dependancy import admin
from fastapi import APIRouter,HTTPException
from src.pydantic_schema.task_pydantic import UpdateTask
from src.CRUD.Admin_crud import updateTask

router=APIRouter()

@router.put("/{task_id}")
def taskUpdation(task_id:int,task:UpdateTask,current_user:dict = admin):
    try:
        master=current_user["username"]
        updateTask(task_id=task_id,updateTask=task,master=master)
        return {"message":"Task table updation sucessfully "}
    except HTTPException as e:
        raise e