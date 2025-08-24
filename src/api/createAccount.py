from fastapi import APIRouter,HTTPException,status
from src.pydantic_schema.User_pydantic import UserCreate ,UserOut
from src.Dependancy.dependancy import admin
from  fastapi import HTTPException
from src.CRUD.Admin_crud import new_User

router=APIRouter()
@router.post("/")
def create_account(user: UserCreate, current_user: dict = admin):
    if not user.name.strip() or not user.email.strip() or not user.password.strip() or not user.role.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Empty Input")
        
    try:
        master=current_user["username"]
        new_User(user,master=master)
        return {"detail": "User created successfully"}
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))