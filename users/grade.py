import tools.sqlite as sql
import json

class Grades:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def searchAll(self):
        grade = Grade('',self.user_id,'','','')
        database = sql.DataBase()
        result = database.select('users_grades', grade.getKeys(), 'user_id='+str(self.user_id))
        if result == None:
            grades = [] 
        else:
            grades = []
            for item in result:
                grade = Grade(item[0], item[1], item[2], item[3], item[4])
                grades.append(grade)

        return grades

    def searchOnebyId(self, searchId):
        grade = Grade('',self.user_id,'','','')
        database = sql.DataBase()
        result = database.selectOne('users_grades', grade.getKeys(), 'quiz_id='+str(searchId)+' AND user_id='+str(self.user_id))
        if result == None:
            result = []
        return result

class Grade:
    def __init__(self, id, user_id, quiz_id, data, date_creation):
        self.id = id
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.data = data
        self.date_creation = date_creation

    def register(self):
        database = sql.DataBase()
        self.id = database.insert('users_grades',self.__dict__)
        return True

    def getKeys(self):
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

    def getData(self):
        if not type(self.data) == dict:
            self.data = json.loads(self.data)
        return self.data
    
    def getDataQuestions(self):
        data = self.getData()
        return data['questions']

    def getDataQuestionsOK(self):
        data = self.getData()
        return data['questionsOK']

    def getDataQuestionsNOK(self):
        data = self.getData()
        return data['questionsNOK']

    def getDataQuestionsLog(self):
        data = self.getData()
        return data['questionsLog']

    def getDataQuizName(self):
        data = self.getData()
        return data['quizName']