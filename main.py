import random, os
from users import actions, user
from tools import helpers
helper = helpers.Helpers()
action = actions.Actions()
helper.clean()


answer = ''
while answer != 'out':
    helper.startOptions()
    answer=input('Give me the number or write out to exit?\r\n')
    try:
        answer=int(answer)
    except:
        pass

    
    if not type(answer) == int:
        helper.printError('You have to write a number', 3.0)
    else:
        if answer == 1:
            # Register
            action.register()
            break
        elif answer == 2:
            # Login
            action.login()
            break
        else:
            helper.printError('You have to write a correct number from the options bellow', 3.0)
