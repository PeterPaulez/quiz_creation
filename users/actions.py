import tools.helpers as helpers
import users.user as user
import quiz.actions as quizActions
helper = helpers.Helpers()
quizAction = quizActions.Actions()

class Actions:
    def register(self):
        isdone = False
        while not isdone:
            helper.printOut(helper.printColor("HEADER",'Ok, let\'s register you. I need some data from you'))
            name = input('Please, write your Name?\r\n')
            email = input('Please, write your Email?\r\n')
            email=email.lower()
            password = input('Please, write your Password (At least 6 chars with Letters and Numbers)?\r\n')
            if name == 'out' or email == 'out' or password == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
            elif name != '' and email !='' and password != '':
                emailOk = self.checkEmail(email)
                passOk = self.checkPassword(password)
                if not emailOk:
                    helper.printError(f'Your email: {email} is not a valid email.')
                elif not passOk:
                    helper.printError('You have to write a valid password (At least 6 chars with Letters and Numbers).')
                elif len(name)<=2:
                    helper.printError('You have to write a valid name (At least more than 2 chars).')
                else:
                    isdone = True
                    userData = user.User(0, name, email, password)
                    userData.register()
                    quizAction.quizMenu(userData)
            else:
               helper.printError('You have to file correctly your data or write out to exit (All fields are mandatory).')

    def login(self):
        isdone = False
        while not isdone:
            helper.printOut(helper.printColor("HEADER",'Ok, let\'s login you. I need some data from you'))
            email = input('Please, write your Email?\r\n')
            email=email.lower()
            password = input('Please, write your Password?\r\n')
            if email == 'out' or password == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
            elif email != '' and password != '':
                emailOk = self.checkEmail(email)
                passOk = self.checkPassword(password)
                if not emailOk:
                    helper.printError(f'Your email: {email} is not a valid email.')
                elif not passOk:
                    helper.printError('You have to write a valid password (At least 6 chars with Letters and Numbers).')
                else:
                    userData = user.User(0, '', email, password)
                    isdone = userData.login()
                    if not isdone:
                        helper.printError('There is not any user with this email and password.', 6.0)
                    else:
                        quizAction.quizMenu(userData)
            else:
               helper.printError('You have to file correctly your data or write out to exit.')
    
    def checkEmail(self, email):
        import re
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email = email.lower()
        if re.search(regex,email):
            return True
        else:
            return False
    
    def checkPassword(self, password):
        if len(password)>=6 and password.isalnum():
            return True
        else:
            return False
    
            