from pydantic import BaseModel
from src.Enum_modal.Enum import statusEnum
class TaskCreate(BaseModel):
    assigned_to: int
    title: str
    description: str
    status: statusEnum

class UpdateTask(BaseModel):
    assigned_to: int = None
    title: str = None
    description: str = None
    status: statusEnum

class TaskOut(BaseModel):
    id:int

    class Config:
        orm_mode = True