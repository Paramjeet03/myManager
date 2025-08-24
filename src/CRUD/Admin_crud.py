from src.pydantic_schema.User_pydantic import UserCreate,Update_user,EmailStr
from src.pydantic_schema.task_pydantic import TaskCreate,UpdateTask,TaskOut
from src.pydantic_schema.User_log_pydantic import getlog
from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table,User_log,Update_log,delete_log
from src.Auth.Hashing_token import hash_pass
from fastapi import HTTPException,status
from datetime import datetime
from src.Config.Config import setting

def new_User(user:UserCreate,master:str):
        
    db=localSession()
    if db.query(User_table).filter(User_table.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already registered")
    db.add(User_table(name=user.name, email=user.email, pass_hash=hash_pass(user.password), role=user.role,phone=user.phone,create_by=master))
    db.commit()
    db.close()



def Update_user_table(user: Update_user,master:str):
    db=localSession()
    user_in_db = db.query(User_table).filter(User_table.email.ilike(user.email)).first()
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    updated = False

    if user.role is not None and user.role.strip() !="":
        user_in_db.role = user.role
        updated = True

    if user.name is not None and user.name.strip() !="":
        user_in_db.name = user.name
        updated = True

    if updated:
        data=Update_log(update_user=user_in_db.email,Updatedby=master)
        db.add(data)
        db.commit()
        db.close()
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No values provided for update")
    
def delete_user_table(user_email:EmailStr,master:str):
    db=localSession()
    user_in_db = db.query(User_table).filter(User_table.email == user_email).first()
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    if user_in_db.email=="Rootadmin@example.com":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allowed to delete Root admin")
    else:
        db.delete(user_in_db)
        data=delete_log( delete_user=user_in_db.email,deleteBy=master)
        db.add(data)
        db.commit()

def get_user(user_email:EmailStr):
    db=localSession()
    user = db.query(User_table).filter(User_table.email == user_email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist or Wrong Email")
    else:
        return {"id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "phone": user.phone,
        "create_by": user.create_by}
    
def assignTask(task:TaskCreate,master:str):
    db=localSession()
    mail=db.query(User_table).filter(User_table.id == task.assigned_to).first().email
    if not db.query(User_table).filter(User_table.id == task.assigned_to).first():
        raise HTTPException(status_code=400,detail="User id not exist !!")
    if mail.strip().lower()==setting.SUPER_MAIL:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not allow")
    else:
        data=Task_table(**task.dict(),given_by=master)
        db.add(data)
        db.commit()


def updateTask(task_id: int, updateTask: UpdateTask,master:str):
    db = localSession()
    user_in_db = db.query(Task_table).filter(Task_table.idx == task_id).first()
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task id does not exist in task database")

    updated = False

    if updateTask.assigned_to is not None :
        assigned_user = db.query(User_table).filter(User_table.id == updateTask.assigned_to).first()
        if not assigned_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assigned user does not exist in Main Database")
        user_in_db.assigned_to = updateTask.assigned_to
        updated = True

    if updateTask.title is not None and updateTask.title !="":
        user_in_db.title = updateTask.title
        updated = True

    if updateTask.description is not None and updateTask.description !="":
        user_in_db.description = updateTask.description
        updated = True

    if updateTask.status is not None and updateTask.status !="":
        user_in_db.status = updateTask.status
        updated = True

    if updated:
        user_in_db.given_by=master
        user_in_db.given_on = datetime.now()
        db.commit()
        db.close()
        return {"message": "User Task updated successfully"}
    else:
        db.close()
        raise HTTPException(status_code=400, detail="No values provided for update")
    
def deleteTask(out:TaskOut):
    db = localSession()
    user_in_db = db.query(Task_table).filter(Task_table.idx == out.id).first()
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task id does not exist in task database")
    else:
        db.query(Task_table).filter(Task_table.idx==out.id).delete()
        db.commit()
        return {"message":"Delete task sucessfully"}



    
def getlog_admin(log_id:getlog):
    db=localSession()
    data=db.query(User_log.idx,User_table.id,User_table.name,User_table.email,User_log.status,User_log.login_time,User_log.logout_time).join(User_log, User_table.id == User_log.user_id).filter(User_log.user_id==log_id.id).all()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No log added by User")
    else:
        log_ls=[{
            "log_idx":i[0],
            "User_id":i[1],
            "User_Name":i[2],
            "User_email":i[3],
            "status":i[4],
            "login_time":i[5],
            "logout_time":i[6]
        }
        for i in data
        ]
        return log_ls
