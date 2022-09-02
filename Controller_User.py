from DAL_User import DALUser
from DAL_Passwords import DALPasswords
from DAL import Dal
class ControllerUser():
    def __init__(self) -> None:

        self.session = Dal()

        self.sessionUser = DALUser()
        self.sessionPassword = DALPasswords()
    
    def get_list_dict_users(self):
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
        errors = []
        if not self.check_user_has_account(name):
            errors.append("User not registered. Please sign-up.")
            return False, errors
        if not self.check_user_password(name,password):
            errors.append("Password Incorrect. Please try again.")
            return False, errors
            
        return True, errors
        
	
    def check_user_has_account(self, name):

        users = self.get_list_dict_users()
        for user in users:
            if name == user["Name"]:
                return True
        return False
            
    def check_user_password(self, name, password):
        self.sessionUser.open()
        self.sessionPassword.open()

        id = self.sessionUser.get_ID_by_name(name)
        db_password = self.sessionPassword.get_password_by_ID(id)

        self.sessionUser.close()
        self.sessionPassword.close()
        
        return  password == db_password
        
        