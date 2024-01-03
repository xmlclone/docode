from orm_demo1.dal import UserDAL

class UserService:
    def __init__(self):
        self.user_dal = UserDAL()

    def create_user(self, name, email):
        self.user_dal.create_user(name, email)

    def update_user(self, user_id, name):
        self.user_dal.update_user(user_id, name)

    def delete_user(self, user_id):
        self.user_dal.delete_user(user_id)

    def get_user(self, user_id):
        return self.user_dal.get_user(user_id)

    def get_all_users(self):
        return self.user_dal.get_all_users()