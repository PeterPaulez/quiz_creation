import tools.helpers as helpers
import users.user as user
import quiz.quiz as quiz
import datetime
dateNowFull=datetime.datetime.now()
dateNowShort=dateNowFull.strftime("%Y-%m-%d")
helper = helpers.Helpers()

class Actions:
    def quizMenu(self, user):        
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
                    self.quizNew(user)
                    break
                elif answer == 2:
                    # Do a Quiz
                    self.quizDo(user)
                    break
                elif answer == 3:
                    # Search a Quizz
                    self.quizSearch(user)
                    break
                elif answer == 4:
                    # List your Quizzes
                    self.quizList(user)
                    break
                elif answer == 5:
                    # List your Grades
                    self.quizGrades(user)
                    break
                elif answer == 6:
                    # Exit
                    helper.printOut('Good Bye, I am here to server you!')
                    break
                else:
                    helper.printError('You have to write a correct number from the options bellow')

    def quizNew(self, user):
        isdone = False
        while not isdone:
            helper.printOut(helper.printColor("HEADER",'Ok, let\'s create a new Quiz. I need some data from you'))
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

            if quizName == 'out':
                isdone = True
                helper.printOut('Good Bye, I am here to server you!')
                self.quizMenu(user)
            elif quizName != '' and quizTypeId != 0 and quizQuestions != 0:
                if quizTypeId != 1 and quizTypeId != 2:
                    helper.printError(f'You choose a wrong type of Quiz, try again writting 1 or 2.')
                elif quizQuestions < 5 or quizQuestions > 20:
                    helper.printError(f'You choose a wrong number of random Questions, try again writting a number range from 5 to 20.')
                elif len(quizName)<=6 or not quizNameTrim.isalnum():
                    helper.printError(f'You have to write a valid title for your Quiz (At least more than 6 chars [{quizName}]).')
                else:
                    isdone = True
                    helper.printError('Your Quiz is created, now you have to add questions and correct answers.',2.0)
                    quizData = quiz.Quiz('', user.id, quizName, quizTypeId, quizQuestions, '', dateNowShort)
                    quizData.register()
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
                    self.quizMenu(user)
            else:
                if answer == 1:
                    # Edita Quiz Data
                    #self.quizEditData(user)
                    break
                elif answer == 2:
                    # Add Quiz Questions
                    self.quizAddQuestions(user, quiz)
                    break
                elif answer == 3:
                    # Edit Quiz Questions
                    #self.quizEditQuestions(user)
                    break
                elif answer == 4:
                    # Delete Quiz Questions
                    #self.quizDeleteQuestions(user)
                    break
                elif answer == 5:
                    # Exit
                    helper.printOut('Good Bye, I am here to server you!')
                    self.quizMenu(user)
                    break
                else:
                    helper.printError('You have to write a correct number from the options bellow')
    
    def quizAddQuestions(self, user, quiz):
        isdone = False
        contador = 0
        while not isdone:
            contador += 1
            helper.printOut(helper.printColor("HEADER",'Ok, let\'s create a new Question. I need some data from you'))
            if quiz.data == '':
                quiz.data = []
            quizQuestion = input('Please, write the Question of the Quiz?\r\n')
            quizQuestionTrim = quizQuestion.replace(" ", "")
            quizAnswer = input('Please, write the correct Answer of the Quiz?\r\n')
            quizAnswerTrim = quizAnswer.replace(" ", "")
            if len(quizQuestion)<=6 or not quizQuestionTrim.isalnum():
                helper.printError(f'You have to write a valid Question (At least more than 6 chars [{quizQuestion}]).')
            elif len(quizAnswer)<=1 or not quizAnswerTrim.isalnum():
                helper.printError(f'You have to write a valid Answer (At least more than 1 char [{quizAnswer}]).')
            else:
                quiz.data.append({'question':quizQuestion, 'correctAnswer':quizAnswer})
                quiz.updateQuestions()
                helper.printError('Your Question is Added, continue adding or write out to exit.',2.0)

            if quizQuestion.lower() == 'out':
                isdone = True
                helper.printError(f'Your new Questions are added to your Quiz.')
                self.quizMenu(user)

    def quizSearch(self, user):
        isdone = False
        while not isdone:
            helper.printOut(helper.printColor("HEADER",'Ok, let\'s search into the Quizzes. I need some data from you'))
            quizName = input('Please, write the Title of the Quiz?\r\n')
            quizNameTrim = quizName.replace(" ", "")
            if len(quizName)<=6 or not quizNameTrim.isalnum():
                helper.printError('You have to write a valid title for your Quiz (At least more than 6 chars).')
            else:
                isdone = True
                helper.printError('Your Quiz is created and you can give a try searching it.')
                self.quizMenu(user)
 
    def quizList(self, user):
        helper.printOut(f'List Quiz! {user.name}')

    def quizGrades(self, user):
        helper.printOut(f'List Grades! {user.name}')

    def quizDo(self, user):
        helper.printOut(f'Do Quiz! {user.name}')

