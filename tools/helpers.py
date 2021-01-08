import os, time

class Helpers:
    def getSeparator(self):
        return '=============================================================================='

    def clean(self):
        os.system('cls||clear')

    def printOut(self,msg):
        self.clean()
        print(self.getSeparator())
        print(msg)
        print(self.getSeparator())
    
    def printError(self, msg, sleepTime):
        print(self.getSeparator())
        print(msg)
        print(self.getSeparator())
        time.sleep(sleepTime)
    
    def startOptions(self):
        options = f'Welcome to Quiz Creator APP\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        1) Register
        2) Login
        '''
        self.printOut(options)

    def loggedOptions(self, user):
        options = f'Welcome to Quiz Creator APP ({user.name})\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        1) View your Quizzes
        2) Search a Quiz
        3) Create a new Quiz
        4) Edit a Quiz
        5) Delete a Quiz
        6) View your grades
        '''
        self.printOut(options)