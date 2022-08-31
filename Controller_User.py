from DAL_User import DALUser
from DAL_Passwords import DALPasswords
from DAL import Dal
class ControllerUser():
    def __init__(self) -> None:

        self.session = Dal()

        self.sessionUser = DALUser()
        self.sessionPassword = DALPasswords()
    
    def get_list_users(self):
        self.sessionUser.open()
        users = self.sessionUser.get_users()
        self.sessionUser.close()
        return users

    def create_user(self, name, password):
        self.sessionUser.open()
        id = self.sessionUser.create_user(name)
        self.sessionUser.close()

        self.sessionPassword.open()
        self.sessionPassword.save_password(id,password)
        self.sessionPassword.close()

    def check_login(self, name, password):
        pass
	
    