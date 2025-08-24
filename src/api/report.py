from src.CRUD.reportCrud import report_db
from fastapi import APIRouter
from src.Dependancy.dependancy import both

router=APIRouter()

@router.get("/")
def report(current_user:dict = both):
    return report_db()