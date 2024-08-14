from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建一个连接到 SQLite 数据库的引擎
engine = create_engine('sqlite:///sample.db', echo=True)

# 创建一个基类，用于定义 ORM 类
Base = declarative_base()

# 定义一个 ORM 类
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"

# 创建表
Base.metadata.create_all(engine)

# 创建一个会话类
Session = sessionmaker(bind=engine)

# 使用会话类创建一个会话对象
session = Session()

# 添加一个用户
user = User(name="Alice", age=20)
session.add(user)
session.commit()

# 查询所有用户
all_users = session.query(User).all()
print(all_users)