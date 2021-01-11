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
    
    def printError(self, msg, sleepTime=3):
        print(self.getSeparator())
        print(msg)
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
        options = f'{self.printColor("HEADER","Welcome to Quiz Creator APP")} ({self.printColor("UNDERLINE", user.name)} - {self.printColor("UNDERLINE", str(user.id))})\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        '''+self.printColor("WARNING","1)")+''' Create a new Quiz
        '''+self.printColor("WARNING","2)")+''' Do a Quiz
        '''+self.printColor("WARNING","3)")+''' Edit a Quiz
        '''+self.printColor("WARNING","4)")+''' List your Quizzes
        '''+self.printColor("WARNING","5)")+''' View your grades
        '''+self.printColor("WARNING","6)")+''' Exit
        '''
        self.printOut(options)

    def quizOptions(self, quiz):
        options = f'{self.printColor("HEADER","It is the time to edit your Quiz:")} ({self.printColor("UNDERLINE", quiz.name)} - {self.printColor("UNDERLINE", str(quiz.id))})\r\n{self.getSeparator()}\r\n'
        options += '''        
        What do you want to do?
        '''+self.printColor("WARNING","1)")+''' Edit data of your Quiz
        '''+self.printColor("WARNING","2)")+''' Add new Questions
        '''+self.printColor("WARNING","3)")+''' Edit Questions
        '''+self.printColor("WARNING","4)")+''' Delete Questions
        '''+self.printColor("WARNING","5)")+''' Exit
        '''
        self.printOut(options)