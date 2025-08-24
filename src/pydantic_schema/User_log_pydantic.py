from pydantic import BaseModel
from datetime import datetime

class add_log(BaseModel):
    task_id:int
    status:str
    login_time:datetime

class getlog(BaseModel):
    id:int

class Config:
    from_attributes = True