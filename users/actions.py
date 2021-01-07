# Al hacer el import tengo que mentar 'users' que es el paquete
import users.helpers as helpers
helper = helpers.Helpers() 

class Actions:
    def Register(self):
        isdone = False
        while not isdone:
            helper.printOut('Ok, let\'s register you. I need some data from you')
            name = input('Please, write your Name?\r\n')
            email = input('Please, write your Email?\r\n')
            password = input('Please, write your Password (At least 6 chars with Letters and Numbers)?\r\n')
            if name == 'out' or email == 'out' or password == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
            elif name != '' and email !='' and password != '':
                isdone = True
                helper.printOut('Your registration is ok and you are just logged')
            else:
               helper.printError('You have to file correctly your data or write out to exit.', 2.0)

    def Login(self):
        isdone = False
        while not isdone:
            helper.printOut('Ok, let\'s login you. I need some data from you')
            name = input('Please, write your Email?\r\n')
            password = input('Please, write your Password?\r\n')
            if name == 'out' or password == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
            elif name != '' and password != '':
                isdone = True
                helper.printOut('You are just logged')
            else:
               helper.printError('You have to file correctly your data or write out to exit.', 2.0)
    
            