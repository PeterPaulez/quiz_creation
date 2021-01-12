import tools.sqlite as sql
import json

class Quizzes:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def searchAll(self):
        quiz = Quiz('',self.user_id,'','','','','')
        database = sql.DataBase()
        result = database.select('quizzes', quiz.quizKeys(), 'user_id='+str(self.user_id))
        if result == None:
            quizzes = [] 
        else:
            quizzes = []
            for item in result:
                quiz = Quiz(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
                quizzes.append(quiz)

        return quizzes
        
    def searchOnebyName(self, searchStr):
        quiz = Quiz('',self.user_id,'','','','','')
        database = sql.DataBase()
        result = database.selectOne('quizzes', quiz.quizKeys(), 'name LIKE "%'+searchStr+'%" ORDER BY user_id='+str(self.user_id)+' DESC')
        if result == None:
            result = []
        return result

    def searchOnebyId(self, searchId):
        quiz = Quiz('',self.user_id,'','','','','')
        database = sql.DataBase()
        result = database.selectOne('quizzes', quiz.quizKeys(), 'id='+str(searchId)+' AND user_id='+str(self.user_id))
        if result == None:
            result = []
        return result

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
        if type(self.data) == dict:
            self.data = json.dumps(self.data)
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

    def getTotalQuestions(self):
        if self.data == '':
            return 0
        else:
            if not type(self.data) == list:
                self.data = json.loads(self.data)
            return len(self.data)

    def getUserName(self):
        database = sql.DataBase()
        result = database.selectOne('users','name','id='+str(self.user_id))
        return result[0]
