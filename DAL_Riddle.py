import DAL

tablename = 'Riddles'

class DALRiddle(DAL.Dal):
    def __init__(self) -> None:
        super().__init__()


    def get_riddle_last(self):
        self.cursor.execute(f"select * from riddles order by id desc limit 1")
        return self.cursor.fetchone()

    def get_riddle_ID(self, id):
        self.cursor.execute(f"SELECT * FROM Riddles where id = {id}")
        return  self.cursor.fetchone()
