import tools.helpers as helpers
import users.user as userModel
import quiz.quiz as quizModel
import datetime, json, random, time
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
                elif answer == 4: # TODO
                    # Delete your Quizzes
                    #self.quizzesDelete(user)
                    break
                elif answer == 5: # TODO
                    # List your Grades
                    self.quizzesGrades(user)
                    break
                elif answer == 6:
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
            if quizName.lower() == 'out':
                isdone = True
                self.quizzesMenu(user)
            elif not helper.stringOk(quizName, 3):
                helper.printError('You have to write a valid title for your Quiz (At least more than 4 chars).')
            else:             
                quizzes = quizModel.Quizzes(user.id)
                result = quizzes.searchOnebyName(quizName)
                if not len(result) == 0:
                    helper.printOk('There is a Quiz which contains "'+quizName+'", Let`s go.',1.0)
                    isdone = True 
                    quizData = quizModel.Quiz(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
                    self.quizEdit(user, quizData)
                else:
                    helper.printError('There is not Quiz containing name: '+quizName)
 
    def quizzesList(self, user):
        isdone = False
        while not isdone:
            options = f'{helper.printColor("HEADER","List of your Quizzes:")} ({helper.printColor("UNDERLINE", user.name)})'
            helper.printOut(options)
            quizzes = quizModel.Quizzes(user.id)
            result = quizzes.searchAll()
            for item in result:
                print(f'{helper.printColor("WARNING",f"{item.id})")} {item.name}')
            print(helper.getSeparator())
            answer = input('Please, write the ID of the Quiz to edit it:\r\n')
            try:
                answer = int(answer)
            except:
                pass
            
            if not type(answer) == int:
                if not answer == 'out':
                    helper.printError('You have to write a number')
                else:
                    isdone = True 
                    self.quizzesMenu(user)
            else:
                result = quizzes.searchOnebyId(answer)
                if not len(result) == 0:
                    isdone = True 
                    quizData = quizModel.Quiz(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
                    self.quizEdit(user, quizData)
                else:
                    helper.printError('There is not Quiz having ID: '+str(answer))

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
                elif not helper.stringOk(quizName, 6):
                    helper.printError(f'You have to write a valid title for your Quiz (At least more than 6 chars [{quizName}]).')
                else:
                    isdone = True
                    if isNew == True:
                        helper.printOk('Your Quiz is created, now you have to add questions and correct answers.')
                        quizData = quizModel.Quiz('', user.id, quizName, quizTypeId, quizQuestions, '', dateNowShort)
                        quizData.register()
                    else:
                        helper.printOk('Your Quiz is edited.')
                        quizData = quizModel.Quiz(quiz.id, quiz.user_id, quizName, quiz.type_id, quizQuestions, quiz.data, quiz.date_creation)
                        quizData.update()
                    self.quizEdit(user,quizData)
            else:
                helper.printError('You have to file correctly your data or write out to exit (All fields are mandatory).')

    def quizEdit(self, user, quiz):
        answer = ''
        while answer != 'out':
            helper.quizOptions(quiz)
            answer=input('Give me the number or write out to Back?\r\n')
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
                    self.quizDo(user,quiz)
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
                    # Back
                    helper.printOut('Good Bye, I am here to server you!')
                    self.quizzesMenu(user)
                    break
                else:
                    helper.printError('You have to write a correct number from the options bellow')
    
    def quizEditData(self, user, quiz):
        if not quiz.user_id == user.id:
            helper.printError('You are not the owner of this QUIZ, so there is not possible to edit it')
            self.quizEdit(user, quiz)
        else:
            self.quizzesData(user, quiz)

    def quizAddQuestions(self, user, quiz):
        if not quiz.user_id == user.id:
            helper.printError('You are not the owner of this QUIZ, so there is not possible to edit it')
            self.quizEdit(user, quiz)
        else:
            isdone = False
            while not isdone:
                quizInputs = []
                quizQuestion = ''
                quizAnswer = ''
                helper.printHeader('Ok, let\'s create a new Question. I need some data from you')
                quizQuestion = input('- Please, write the Question of the Quiz?\r\n')
                if not quizQuestion.lower() == 'out' and "FILE:" in quizQuestion:
                    quizQuestionstr = quizQuestion.split(':')
                    fileName = './data/'+quizQuestionstr[1]
                    from csv import reader
                    with open(fileName, 'r', encoding='utf-8') as content:
                        csv_reader = reader(content)
                        for line in csv_reader:
                            quizQuestionLine = line[0]
                            quizAnswerLine = line[1]
                            print(quizQuestionLine+' => '+quizAnswerLine)
                            quizInputs.append({'question':quizQuestionLine, 'answer':quizAnswerLine})
                    isdone = True
                    self.quizAddQuestionsDecide(user, quiz, quizInputs)
                    self.quizEdit(user,quiz)
                else:
                    if not quizQuestion.lower() == 'out':
                        quizAnswer = input('- Please, write the correct Answer of the Quiz?\r\n')
                        quizInputs.append({"question":quizQuestion, "answer":quizAnswer})
                        self.quizAddQuestionsDecide(user, quiz, quizInputs)
                    # Decide what to do after INPUTs
                    if quizQuestion.lower() == 'out' or quizAnswer.lower() == 'out':
                        isdone = True
                        self.quizEdit(user,quiz)

    def quizAddQuestionsDecide(self, user, quiz, quizInputs):
        for quizInput in quizInputs:
            quizQuestion = quizInput['question']
            quizAnswer = quizInput['answer']
            if not helper.stringOk(quizQuestion, 6):
                helper.printError(f'You have to write a valid Question (At least more than 6 chars [{quizQuestion}]).')
            elif not helper.stringOk(quizAnswer, 1):
                helper.printError(f'You have to write a valid Answer (At least more than 1 char [{quizAnswer}]).')
            else:
                if quiz.data == '':
                    quiz.data = []
                elif type(quiz.data) == str:
                    quiz.data = json.loads(quiz.data)
                quiz.data.append({"question":quizQuestion, "correctAnswer":quizAnswer})
                quiz.updateQuestions()
                helper.printOk('Your Question is Added, continue adding or write out to exit.',0.5)

    def quizDo(self, user, quiz):
        # QuizData json String
        if quiz.data == '':
            self.quizEdit(user,quiz)
            return
        elif type(quiz.data) == str:
            questions = json.loads(quiz.data)
        else:
            questions = quiz.data

        # Start the test
        questionsOK = 0
        questionsKO = 0
        failStr = ''
        random.shuffle(questions)
        questionsDone = 0
        isDone = False
        while not isDone:    
            for question in questions:
                # Important data
                questionStr = question['question']
                correctAnswer = question['correctAnswer']

                # Final del test
                questionsDone += 1
                if questionsDone == quiz.questions + 1:
                    isDone = True
                    break
                
                # Respuesta según tipo test
                if quiz.type_id == 2 :
                    random.shuffle(question['respuestas'])
                    #contador = 0
                    #for respuesta in question['respuestas']:
                    #    contador += 1
                    #    #print(f'{bcolors.WARNING}{contador}){bcolors.ENDC} {respuesta}')
                    #respuesta = input(f'{preguntasDone}.- {pregunta} [{bcolors.OKGREEN}Escribe el número de la respuesta correcta{bcolors.ENDC} ({bcolors.OKBLUE}Escribe out para salir{bcolors.ENDC})]\r\n{separador}\r\n')
                else:
                    helper.clean()
                    print(helper.getSeparator())
                    answer = input(helper.printColor("OKBLUE", str(questionsDone)+'.- '+questionStr+'?')+'\r\n'+helper.getSeparator()+'\r\n')
                    #answer=input(str(questionsDone)+'.- '+questionStr+'?\r\n')

                if correctAnswer.lower() == answer.lower():
                    questionsOK += 1
                else:
                    failStr += "\n - "+questionStr+": "+helper.printColor('FAIL',answer)+" ---> "+helper.printColor('OKGREEN',correctAnswer)
                    questionsKO += 1

        helper.clean()
        helper.printOk(f'Your result is {questionsOK} of {quiz.questions}',0)
        if not failStr == '':
            print(helper.printColor("FAIL",f'You failed the next questions [{questionsKO}]')+':'+failStr)
            print(helper.getSeparator())

        time.sleep(5)
        input('Press ENTER or any KEY to continue!')
        self.quizEdit(user,quiz)