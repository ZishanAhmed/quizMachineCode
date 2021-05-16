
import models.question

class quiz:
    def __init__(self,id, name, description, created_by, questions_list):
        self.id = id
        self.name = name
        self.description = description
        self.created_by = created_by
        self.question_id_list = questions_list

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_created_by(self):
        return self.created_by
    
    def get_questions_list(self):
        return self.question_id_list

    def add_question(self, question_id):
        question_id_list.append(question_id)

    def update_quiz_id(self):
        for question in self.question_id_list:
            question.updateQuizId(self.id)
    
