import models.quiz

class question:
    def __init__(self, id, name, description, options):
        self.question_id = id
        self.name = name
        self.description = description
        self.quiz_ids = []
        self.options = options
        self.correct = None

    def get_question_id(self):
        return self.question_id

    def updateQuizId(self,quiz_id):
        self.quiz_ids.append(quiz_id)
    
    # answer will be the index of the list
    def updateAnswer(self, answer):
        self.correct = answer
    
    def validateAnswer(self, answer):
        return self.correct==answer
    


    