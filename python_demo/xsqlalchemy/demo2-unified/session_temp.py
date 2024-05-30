from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


DB_URI = "sqlite+pysqlite:///:memory:"
ECHO = False
engine = create_engine(
    DB_URI, 
    echo=ECHO,  # 输出 sqlalchemy 日志
)


class Base(DeclarativeBase):
    pass