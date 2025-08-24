from fastapi import APIRouter, HTTPException, status
from src.Database.session import localSession
from src.Database.db_model import User_table, Task_table
from src.Dependancy.dependancy import admin

router = APIRouter()

@router.get("/")
def get_Task(current_user:dict=admin):
    db = localSession()
    
    # Admin wants to fetch all tasks
    tasks = (
        db.query(
            Task_table.idx,
            Task_table.assigned_to,
            User_table.name,
            User_table.email,
            Task_table.title,
            Task_table.description,
            Task_table.status,
            Task_table.given_on,
            Task_table.given_by
        )
        .join(User_table, User_table.id == Task_table.assigned_to)
        .all()
    )

    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks found!")

    return [
        {
            "task_id": t[0],
            "assigned_to": t[1],
            "name": t[2],
            "email": t[3],
            "title": t[4],
            "description": t[5],
            "status": t[6],
            "given_on": t[7],
            "given_by": t[8]
        }
        for t in tasks
    ]


    

    