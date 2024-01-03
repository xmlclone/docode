from .base import BaseDAL
from orm_demo1.models import User

class UserDAL(BaseDAL):
    def create_user(self, name, email):
        user = User(name=name, email=email)
        self.session.add(user)
        self.commit()

    def update_user(self, user_id, name):
        user = self.session.query(User).filter_by(id=user_id).first()
        user.name = name
        self.commit()

    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        self.session.delete(user)
        self.commit()

    def get_user(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_all_users(self):
        return self.session.query(User).all()