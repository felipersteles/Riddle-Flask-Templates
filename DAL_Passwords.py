import datetime
import DAL

tablename = 'Passwords'

class DALPasswords(DAL.Dal):
    


    def __init__(self) -> None:
        super().__init__()


        
    def save_password(self,ID, password):
        self.cursor.execute(f"INSERT INTO {tablename} VALUES ({ID},'{password}') ; ")
        self.connection.commit()