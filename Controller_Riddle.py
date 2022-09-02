from DAL_Riddle import DALRiddle


class ControllerRiddle():
    def __init__(self) -> None:
        
        self.sessionRiddle = DALRiddle()

    
    def get_riddle_last(self):
        self.sessionRiddle.open()
        riddle = self.sessionRiddle.get_riddle_last()
        self.sessionRiddle.close()
        return riddle
    

