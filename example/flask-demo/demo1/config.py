import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or f"sqlite:///{Path('.').absolute()/ 'instance' / 'demo1.db'}"