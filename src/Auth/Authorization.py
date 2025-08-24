from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt,JWTError
from src.Config.Config import setting
from src.Auth.Hashing_token import oauth2_scheme

def token_decode( token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
            username: str = payload.get("username")
            role: str = payload.get("role")
            if username is None or role is None:
                raise HTTPException(status_code=401, detail="Invalid token !!")
            return {"username": username, "role": role}
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
        


         