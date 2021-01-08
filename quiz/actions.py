import tools.helpers as helpers
import users.user as user
helper = helpers.Helpers()

class Actions:
    def quizMenu(self, user):        
        answer = ''
        while answer != 'out':
            helper.loggedOptions(user)
            answer=input('Give me the number or write out to exit?\r\n')
