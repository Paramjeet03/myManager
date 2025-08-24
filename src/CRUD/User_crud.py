from src.pydantic_schema.User_pydantic import UserLogin
from src.pydantic_schema.User_log_pydantic import add_log,getlog
from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table,User_log
from src.pydantic_schema.task_pydantic import TaskOut
from fastapi import HTTPException,status


def get_user(login:UserLogin):
    db=localSession()
    data=db.query(User_table).filter(User_table.email==login.email).first()
    db.close()
    return data

def getTask(user_id: int):
    db = localSession()
    try:
        user = db.query(User_table).filter(User_table.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User ID does not exist!")

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
            .join(User_table)
            .all()
        )

        if not tasks:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No task assigned to User ID!")

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

    finally:
        db.close()

def get_user_id(name:str):
    db = localSession()
    try:
        result = db.query(User_table.id).filter(User_table.name == name).first()
        if result:
            return result[0]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    finally:
        db.close()

def getusermail(name: str):
    db= localSession()
    try:
        result = db.query(User_table.email).filter(User_table.name == name).first()
        if result:
            return result[0]
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
    finally:
        db.close()
        
def addLog(log: add_log,name:str):
    db = localSession()
    result=get_user_id(name=name)
    data=db.query(Task_table).filter(Task_table.idx == log.task_id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Task id")
    else:
        log_data = User_log(user_id=result, **log.dict())
        db.add(log_data)
        db.commit()
        db.close()
        return {"message": "Log added successfully"}
        

def updatelog(log: add_log,name:str):
    db = localSession()
    id=get_user_id(name=name)
    data = db.query(User_log).filter(User_log.user_id == id).order_by(User_log.idx.desc()).first()
    
    if not data:
        raise HTTPException(status_code=401, detail="There is no previously added log from this ID")
    if log.status:
        data.status = log.status
    if log.login_time:
        data.login_time = log.login_time

    db.commit()
    db.close()
    return {"message": "Log updated successfully"}


def getlog_user(id:int):
    db=localSession()
    data = db.query(
    User_log.idx,
    User_table.name,
    User_table.email,
    User_log.status,
    User_log.login_time,
    User_log.logout_time
).join(User_table, User_log.user_id == User_table.id)\
 .filter(User_log.user_id == id).all()
    db.close()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No log added by User")
    else:
        log_ls=[{
            "log_idx":i[0],
            "User_name":i[1],
            "User_email":i[2],
            "status":i[3],
            "login_time":i[4],
            "logout_time":i[5]
        }
        for i in data
        ]
        return log_ls    

