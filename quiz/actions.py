import tools.helpers as helpers
import users.user as userModel
import quiz.quiz as quizModel
import datetime, json
dateNowFull=datetime.datetime.now()
dateNowShort=dateNowFull.strftime("%Y-%m-%d")
helper = helpers.Helpers()

class Actions:
    def quizzesMenu(self, user):        
        answer = ''
        while answer != 'out':
            helper.loggedOptions(user)
            answer=input('Give me the number or write out to exit?\r\n')
            try:
                answer=int(answer)
            except:
                pass
            
            if not type(answer) == int:
                if not answer == 'out':
                    helper.printError('You have to write a number')
                else:
                    helper.printOut('Good Bye, I am here to server you!')
            else:
                if answer == 1:
                    # Create a new Quiz
                    self.quizzesNew(user)
                    break
                elif answer == 2:
                    # Search a Quizz
                    self.quizzesSearch(user)
                    break
                elif answer == 3:
                    # List your Quizzes
                    self.quizzesList(user)
                    break
                elif answer == 4:
                    # List your Grades
                    self.quizzesGrades(user)
                    break
                elif answer == 5:
                    # Exit
                    helper.printOut('Good Bye, I am here to server you!')
                    break
                else:
                    helper.printError('You have to write a correct number from the options bellow')

    def quizzesNew(self, user):
        self.quizzesData(user, '')

    def quizzesSearch(self, user):
        isdone = False
        while not isdone:
            helper.printHeader('Ok, let\'s search into the Quizzes. I need some data from you')
            quizName = input('Please, write the Title of the Quiz?\r\n')
            quizNameTrim = quizName.replace(" ", "")
            if quizName.lower() == 'out':
                isdone = True
                self.quizzesMenu(user)
            elif len(quizName)<=4 or not quizNameTrim.isalnum():
                helper.printError('You have to write a valid title for your Quiz (At least more than 4 chars).')
            else:             
                quizData = quizModel.Quiz('', user.id, quizName, 0, 0, '', dateNowShort)
                result = quizData.searchOne()
                if not len(result) == 0:
                    helper.printOk('There is a Quiz which contains "'+quizName+'", Let`s go.')
                    isdone = True 
                    quizData = quizModel.Quiz(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
                    self.quizEdit(user, quizData)
                else:
                    helper.printError('There is not Quiz containing name: '+quizName)
 
    def quizzesList(self, user):
        helper.printOut(f'List Quiz! {user.name}')
        self.quizzesMenu(user)

    def quizzesGrades(self, user):
        helper.printOut(f'List Grades! {user.name}')
        self.quizzesMenu(user)
    
    def quizzesData(self, user, quiz=''):
        isdone = False
        while not isdone:
            if quiz == '':
                isNew = True
                msg = 'Ok, let\'s create a new Quiz. I need some data from you'
            else:
                isNew = False
                msg = 'Ok, let\'s edit your Quiz ['+quiz.name+']. I need some data from you'
            helper.printHeader(msg)
            quizName = input('Please, write the Title of the Quiz?\r\n')
            quizNameTrim = quizName.replace(" ", "")
            quizTypeId = input(f'Please, write the Type of the Quiz?\r\n\t{helper.printColor("WARNING","1)")} Write the answer\r\n\t{helper.printColor("WARNING","2)")} Choose the correct answer\r\n')
            quizQuestions = input('Please, write the Number of random Questions of the Quiz 5-20?\r\n')
            try:
                quizTypeId=int(quizTypeId)
                quizQuestions=int(quizQuestions)
            except:
                quizTypeId=0
                quizQuestions=0

            # Decide what to do after INPUTs
            if quizName.lower() == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
                self.quizzesMenu(user)
            elif quizName != '' and quizTypeId != 0 and quizQuestions != 0:
                if quizTypeId != 1 and quizTypeId != 2:
                    helper.printError(f'You choose a wrong type of Quiz, try again writting 1 or 2.')
                elif quizQuestions < 5 or quizQuestions > 20:
                    helper.printError(f'You choose a wrong number of random Questions, try again writting a number range from 5 to 20.')
                elif len(quizName)<=6 or not quizNameTrim.isalnum():
                    helper.printError(f'You have to write a valid title for your Quiz (At least more than 6 chars [{quizName}]).')
                else:
                    isdone = True
                    if isNew == True:
                        helper.printOk('Your Quiz is created, now you have to add questions and correct answers.')
                        quizData = quizModel.Quiz('', user.id, quizName, quizTypeId, quizQuestions, '', dateNowShort)
                        quizData.register()
                    else:
                        helper.printOk('Your Quiz is edited.')
                        quizData = quizModel.Quiz(quiz.id, user.id, quizName, quizTypeId, quizQuestions, quiz.data, quiz.date_creation)
                        quizData.update()
                    self.quizEdit(user,quizData)
            else:
                helper.printError('You have to file correctly your data or write out to exit (All fields are mandatory).')

    def quizEdit(self, user, quiz):
        answer = ''
        while answer != 'out':
            helper.quizOptions(quiz)
            answer=input('Give me the number or write out to exit?\r\n')
            try:
                answer=int(answer)
            except:
                pass
            
            if not type(answer) == int:
                if not answer == 'out':
                    helper.printError('You have to write a number')
                else:
                    self.quizzesMenu(user)
            else:
                if answer == 1:
                    # Do Quiz
                    #self.quizDo(user,quiz)
                    self.quizEdit(user,quiz)
                    break
                elif answer == 2:
                    # Edita Quiz Data
                    self.quizEditData(user,quiz)
                    break
                elif answer == 3:
                    # Add Quiz Questions
                    self.quizAddQuestions(user, quiz)
                    break
                elif answer == 4: # TODO
                    # Edit Quiz Questions
                    #self.quizEditQuestions(user)
                    self.quizEdit(user,quiz)
                    break
                elif answer == 5: # TODO
                    # Delete Quiz Questions
                    #self.quizDeleteQuestions(user)
                    self.quizEdit(user,quiz)
                    break
                elif answer == 6:
                    # Exit
                    helper.printOut('Good Bye, I am here to server you!')
                    self.quizzesMenu(user)
                    break
                else:
                    helper.printError('You have to write a correct number from the options bellow')
    
    def quizEditData(self, user, quiz):
        self.quizzesData(user, quiz)

    def quizAddQuestions(self, user, quiz):
        isdone = False
        while not isdone:
            quizQuestion = ''
            quizAnswer = ''
            helper.printHeader('Ok, let\'s create a new Question. I need some data from you')
            if quiz.data == '':
                quiz.data = []
            elif type(quiz.data) == str:
                quiz.data = json.loads(quiz.data)
            quizQuestion = input('Please, write the Question of the Quiz?\r\n')
            quizQuestionTrim = quizQuestion.replace(" ", "")
            if not quizQuestion.lower() == 'out':
                quizAnswer = input('Please, write the correct Answer of the Quiz?\r\n')
                quizAnswerTrim = quizAnswer.replace(" ", "")
            
            # Decide what to do after INPUTs
            if quizQuestion.lower() == 'out' or quizAnswer.lower() == 'out':
                isdone = True
                self.quizEdit(user,quiz)
            elif len(quizQuestion)<=6 or not quizQuestionTrim.isalnum():
                helper.printError(f'You have to write a valid Question (At least more than 6 chars [{quizQuestion}]).')
            elif len(quizAnswer)<=1 or not quizAnswerTrim.isalnum():
                helper.printError(f'You have to write a valid Answer (At least more than 1 char [{quizAnswer}]).')
            else:
                quiz.data.append({'question':quizQuestion, 'correctAnswer':quizAnswer})
                quiz.updateQuestions()
                helper.printOk('Your Question is Added, continue adding or write out to exit.')


