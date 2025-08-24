from fastapi import APIRouter, HTTPException, status
from src.Database.session import localSession
from src.Dependancy.dependancy import admin
from src.Database.db_model import User_table
from src.Config.Config import setting

router = APIRouter()

@router.get("/")
def get_all(current_user: dict= admin):
    db = localSession()
    users_in_db = db.query(User_table).all()

    if not users_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No users found"
        )
    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "phone":user.phone,
            "create_by": user.create_by
        }
        for user in users_in_db
        if user.email.lower() != setting.SUPER_MAIL
    ]