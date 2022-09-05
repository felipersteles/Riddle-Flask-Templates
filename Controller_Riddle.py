from DAL_Riddle import DALRiddle
from Model_Riddle import Riddle


class ControllerRiddle():
    def __init__(self) -> None:
        
        self.sessionRiddle = DALRiddle()

    
    def get_riddle_last(self):
        self.sessionRiddle.open()
        query_result = self.sessionRiddle.get_riddle_last()
        self.sessionRiddle.close()

        riddle = Riddle.dict_to_object(query_result)
        return riddle
    
    def get_riddle_random(self, last_riddle_id = 0):
        if last_riddle_id == 0:
            self.sessionRiddle.open()
            query_result = self.sessionRiddle.get_riddle_random()
            self.sessionRiddle.close()
        else:
            self.sessionRiddle.open()
            query_result = self.sessionRiddle.get_riddle_random_unrepeatable(last_riddle_id)
            self.sessionRiddle.close()

        riddle = Riddle.dict_to_object(query_result)
        return riddle


    def check_riddle_answer(self,riddle_answer, user_answer):
        riddle_answer = riddle_answer.lower()
        user_answer = user_answer.lower()
        if riddle_answer == user_answer:
            return True
        else :
            return False

