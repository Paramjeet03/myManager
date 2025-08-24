from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
import pytz
from src.Database.session import engine
from pydantic import constr


Base=declarative_base()

ISTZ=pytz.timezone("Asia/Kolkata")
class User_table(Base):
    __tablename__ = "User_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100),unique=True)
    pass_hash = Column(String(300),unique=True)
    role = Column(String(50))
    phone=Column(String(15))
    create_by=Column(String(100))
    create_at = Column(DateTime, default=lambda: datetime.now(ISTZ))

    def __repr__(self):
        return f'{"Id": {self.id}, "Name": "{self.name}", "Email": "{self.email}", "Pass_hash": "{self.pass_hash}", "Role": "{self.role}", "Create_at": "{self.create_at}"}'


class Task_table(Base):
    __tablename__ = "Task_table"
    idx = Column(Integer, primary_key=True)
    assigned_to = Column(Integer, ForeignKey("User_table.id"))
    title = Column(String(100))
    description = Column(String(200))
    status = Column(String(50))
    given_on = Column(DateTime, default=lambda: datetime.now(ISTZ))
    given_by=Column(String(100))

    def __repr__(self):
        return f'{{"Idx": {self.idx}, "Assigned_to": {self.assigned_to}, "Title": "{self.title}", "Description": "{self.description}", "Status": "{self.status}", "Given_on": "{self.given_on}","Given_by": "{self.given_by}"}}'


class User_log(Base):
    __tablename__ = "User_log"
    idx = Column(Integer, primary_key=True)
    task_id=Column(Integer)
    user_id = Column(Integer, ForeignKey("User_table.id"))
    status = Column(String(50))
    login_time = Column(DateTime )
    logout_time = Column(DateTime,default=lambda: datetime.now(ISTZ))

    def __repr__(self):
        return f'{{"Idx": {self.idx}, "Id": {self.user_id}, "Status": "{self.status}", "Login": "{self.login_time}", "Logout": "{self.logout_time}"}}'
    
class Update_log(Base):
    __tablename__="updateuserTablelog"
    idx=Column(Integer,primary_key=True)
    update_user=Column(String(100))
    Updatedby=Column(String(100))
    updateTime=Column(DateTime, default=lambda: datetime.now(ISTZ))

class delete_log(Base):
    __tablename__="userTabledeleteLog"
    idx=Column(Integer,primary_key=True)
    delete_user=Column(String(100))
    deleteBy=Column(String(100))
    deleteTime=Column(DateTime, default=lambda: datetime.now(ISTZ))
   

class db_model():
    def __init__(self):
        Base.metadata.create_all(bind=engine)
model_db=db_model()