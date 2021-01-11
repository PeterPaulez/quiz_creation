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

    def update(self):
        database = sql.DataBase()
        quizId = self.id
        data = self.__dict__
        data.pop('id')
        updateStr = ', '.join(['{0}=\'{1}\''.format(key, value) for (key, value) in data.items()])
        self.id = database.update('quizzes', updateStr, 'id='+str(quizId))
        return True

    def updateQuestions(self):
        database = sql.DataBase()
        database.update('quizzes', 'data=\''+json.dumps(self.data)+'\'', 'id='+str(self.id))
        return True
    
    def quizKeys(self):
        keys = self.__dict__.keys()
        separator = ','
        return separator.join(keys)

    def searchOne(self):
        database = sql.DataBase()
        result = database.selectOne('quizzes', self.quizKeys(), 'name LIKE "%'+self.name+'%" ORDER BY user_id='+str(self.user_id)+' DESC')
        return result
