from flask_login import current_user

class UsersPolicy:
    def __init__(self, user=None):
        self.user = user
    
    def view(self):
        return self.user.id == int(current_user.id) or current_user.is_admin()
    
    def view_users_stat(self):
        return current_user.is_admin()

    def view_pages_stat(self):
        return current_user.is_admin()

    def create(self):
        return current_user.is_admin()

    def delete(self):
        return current_user.is_admin()

    def edit(self):
        # print(type(self.user.id), type(current_user.id))
        return self.user.id == int(current_user.id) or current_user.is_admin()

    def show(self):
        return True
    
    def assign_roles(self):
        return current_user.is_admin()
    


