from fastapi import APIRouter,HTTPException,status
from src.Dependancy.dependancy import user
from src.CRUD.Admin_crud import get_user
from src.CRUD.User_crud import getusermail
from src.Config.Config import setting

router = APIRouter()

@router.get("/")
def read_account(current_user: dict = user):
    try:
        mail = getusermail(current_user["username"])
        return get_user(user_email=mail)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    