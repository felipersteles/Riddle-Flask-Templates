import datetime
import DAL

tablename = 'Users'
class DALUser(DAL.Dal):
    def __init__(self) -> None:
        super().__init__()



    def get_next_id(self):
        self.cursor.execute(f"Select MAX(ID) ID from {tablename};")
        result = self.cursor.fetchone()
        id = result["ID"]
        return id + 1

    def create_user(self, name):
        id = self.get_next_id()
        data = datetime.datetime.now()

        self.cursor.execute(f"Insert into {tablename} values ({id},'{name}', NULL , '{data}') ; ")
        self.connection.commit()

        return id
        

    def get_users(self):
        self.cursor.execute(f"Select * from {tablename} ;")
        return self.cursor.fetchall()








