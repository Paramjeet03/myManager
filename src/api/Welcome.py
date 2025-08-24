from fastapi import APIRouter
from src.Database.db_model import db_model

router=APIRouter()
@router.get("/")
def welcome():
    db_model()
    return "Welcome to user and task Managment system !!"