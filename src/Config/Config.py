from pydantic_settings import BaseSettings
class Setting(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    PWD_HASH_ALGO : str
    SUPER_MAIL: str

    model_config = {
        "env_file": ".env"
    }

setting=Setting()