import tools.sqlite as sql
import json

class Quiz:
    def __init__(self, id, user_id, name, type_id, questions, data, date_creation):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.type_id = type_id
        self.questions = questions
        self.data = data
        self.date_creation = date_creation

    def register(self):
        database = sql.DataBase()
        self.id = database.insert('quizzes',self.__dict__)
        return True

    def updateQuestions(self):
        database = sql.DataBase()
        database.update('quizzes', 'data=\''+json.dumps(self.data)+'\'', 'id='+str(self.id))
        return True
