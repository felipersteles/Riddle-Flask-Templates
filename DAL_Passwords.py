import datetime
import DAL

tablename = 'Passwords'

class DALPasswords(DAL.Dal):
    


    def __init__(self) -> None:
        super().__init__()


        
    def save_password(self,ID, password):
        self.cursor.execute(f"INSERT INTO {tablename} VALUES ({ID},'{password}') ; ")
        self.connection.commit()

    def get_password_by_ID(self, id):
        self.cursor.execute(f'SELECT Password From {tablename} where ID = {id}')
        result = self.cursor.fetchone()
        if result:
            return result["Password"]
        return False


