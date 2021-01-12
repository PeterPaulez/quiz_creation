import os, time

class Helpers:
    def getSeparator(self):
        return '=============================================================================='

    def clean(self):
        os.system('cls||clear')

    def printColor(self,color,texto):
        if color == 'HEADER':
            return '\033[95m'+texto+'\033[0m'
        elif color == 'OKBLUE':
            return '\033[94m'+texto+'\033[0m'
        elif color == 'OKCYAN':
            return '\033[96m'+texto+'\033[0m'
        elif color == 'OKGREEN':
            return '\033[92m'+texto+'\033[0m'
        elif color == 'WARNING':
            return '\033[93m'+texto+'\033[0m'
        elif color == 'FAIL':
            return '\033[91m'+texto+'\033[0m'
        elif color == 'ENDC':
            return '\033[0m'+texto+'\033[0m'
        elif color == 'BOLD':
            return '\033[1m'+texto+'\033[0m'
        elif color == 'UNDERLINE':
            return '\033[4m'+texto+'\033[0m'
        else:
            return ''

    def printOut(self,msg):
        self.clean()
        print(self.getSeparator())
        print(self.printColor("OKBLUE",msg))
        print(self.getSeparator())

    def printHeader(self,msg):
        self.clean()
        print(self.getSeparator())
        print(self.printColor("HEADER",msg))
        print(self.getSeparator())
    
    def printError(self, msg, sleepTime=3):
        print(self.getSeparator())
        print(self.printColor("FAIL",msg))
        print(self.getSeparator())
        time.sleep(sleepTime)

    def printOk(self, msg, sleepTime=1):
        print(self.getSeparator())
        print(self.printColor("OKGREEN",msg))
        print(self.getSeparator())
        time.sleep(sleepTime)
    
    def startOptions(self):
        options = f'{self.printColor("HEADER","Welcome to Quiz Creator APP")}\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        '''+self.printColor("WARNING","1)")+''' Register
        '''+self.printColor("WARNING","2)")+''' Login
        '''+self.printColor("WARNING","3)")+''' Exit
        '''
        self.printOut(options)

    def loggedOptions(self, user):
        options = f'{self.printColor("HEADER","Welcome to Quiz Creator APP")}\r\nName: {self.printColor("OKBLUE", user.name)}\r\nEmail: {self.printColor("OKBLUE", user.email)}\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        '''+self.printColor("WARNING","1)")+''' Create a new Quiz
        '''+self.printColor("WARNING","2)")+''' Search a Quiz
        '''+self.printColor("WARNING","3)")+''' List your Quizzes
        '''+self.printColor("WARNING","4)")+''' Delete your Quizzes
        '''+self.printColor("WARNING","5)")+''' View your grades
        '''+self.printColor("WARNING","6)")+''' Exit
        '''
        self.printOut(options)

    def quizOptions(self, quiz):
        options = f'{self.printColor("HEADER","It is the time to edit your Quiz:")}\r\nName: {self.printColor("OKBLUE", quiz.name)}\r\nExam Questions: {self.printColor("OKBLUE", str(quiz.questions))}\r\nTotal Questions: {self.printColor("OKBLUE", str(quiz.getTotalQuestions()))}\r\nOwner: {self.printColor("OKBLUE", str(quiz.getUserName()))}\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        '''+self.printColor("WARNING","1)")+''' Do the Quiz
        '''+self.printColor("WARNING","2)")+''' Edit data of your Quiz
        '''+self.printColor("WARNING","3)")+''' Add new Questions
        '''+self.printColor("WARNING","4)")+''' Edit Questions
        '''+self.printColor("WARNING","5)")+''' Delete Questions
        '''+self.printColor("WARNING","6)")+''' Back
        '''
        self.printOut(options)