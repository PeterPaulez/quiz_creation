import random, os
from users import actions, quiz, user, helpers
helper = helpers.Helpers()
helper.clean()


answer = ''
while answer != 'out':
    helper.startOptions()
    answer=input('Give me the number?\r\n')
    try:
        answer=int(answer)
    except:
        pass

    if not type(answer) == int:
        helper.printError('You have to write a number', 2.0)