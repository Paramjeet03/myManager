from fastapi import APIRouter, HTTPException, status
from src.Database.session import localSession
from src.Database.db_model import User_table, Task_table

router = APIRouter()

@router.get("/")
def taskfmMail(Email: str):
    db = localSession()
    try:
        user = db.query(User_table).filter(User_table.email == Email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User with this email does not exist!"
            )

        user_id = user.id

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
            .filter(Task_table.assigned_to == user_id)
            .join(User_table, User_table.id == Task_table.assigned_to)
            .all()
        )

        if not tasks:
            return {"message": "No tasks assigned to this user.", "tasks": []}

        # Prepare task list
        task_list = [
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

        return {"tasks": task_list}

    finally:
        db.close()