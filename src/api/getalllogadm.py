from src.CRUD.Admin_crud import getlog_admin
from src.pydantic_schema.User_log_pydantic import getlog
from fastapi import APIRouter,HTTPException,status
from src.Dependancy.dependancy import admin
from src.Database.session import localSession
from src.Database.db_model import User_log,User_table

router=APIRouter()

@router.get("/")
def getalllogAdmin():
    db=localSession()
    data=db.query(User_log.idx,User_table.id,User_table.name,User_table.email,User_log.status,User_log.login_time,User_log.logout_time).join(User_log, User_table.id == User_log.user_id).all()
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