class Riddle():
    def __init__(self, ID,Question, Answer, Creator, Active):
        self.ID = ID
        self.question = Question
        self.answer = Answer
        self.creator = Creator
        self.active = Active

    
    def dict_to_object(riddle):
        riddle = Riddle(riddle["ID"],
                riddle["Question"],
                riddle["Answer"],
                riddle["Creator"],
                riddle["Active"] )
        return riddle