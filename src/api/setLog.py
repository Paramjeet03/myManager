from fastapi import APIRouter,HTTPException,status
from src.pydantic_schema.User_log_pydantic import add_log
from src.CRUD.User_crud import addLog
from src.Dependancy.dependancy import user

router=APIRouter()

@router.post("/")
def logSet(log:add_log,current_user:dict=user):
    if not log.status.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Empty Input")
    try :
        addLog(log=log,name=current_user["username"])
        return {"message":"Log added Sucessfully !!}"}
    except HTTPException as e:
        raise e


   