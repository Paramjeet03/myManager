from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.Config.Config import setting

engine=create_engine(setting.DATABASE_URL,echo=True)
localSession=sessionmaker(bind=engine)