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
        options = ''' 
        What do you want to do?
        1) Register
        2) Login
        '''
        self.printOut(options)