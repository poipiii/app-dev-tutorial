#class Question:
#    Questionbank = {}
#    answerbank = {}
#    def __init__(self):
#        self.__question = []
#        self.__answer = []
#    def set_Question(self,question):
#        for i in self.__class__.Questionbank.keys():
#            if i == question:
#                self.__question.append(self.__class__.Questionbank[i])
#            else:
#                pass
#
#    def set_Answer(self,answer):
#        for i in self.__class__.answerbank.keys():
#            if i == answer:
#                self.__answer.append(self.__class__.answerbank[i])
#            else:
#                pass
#    def get_Question(self):
#        return self.__question
#    
#    def get_Answer(self):
#        return self.__answer
#
#
#class Quiz:
#    def __init__(self):
#        self.__playerans = []
#        self.__playerscore = 0
#    def Generate_num(self):
#        import random 
#        return random.randint(1,11)
#
#
#
#testlist = []
#for i in range():
#    rand = Quiz()
#    testlist.append(rand.Generate_num())
#print(testlist)


# import random
# class question:
#     def __init__(self,qus,ans):
#         self.ans = ans
#         self.qus = qus
#
# class quiz:
#     questions = []
#     def __init__(self):
#         self.set_qus()
#         self.points = 0
#     def set_qus(self):
#         q1 = question('can bird fly', 'N')
#         self.__class__.questions.append(q1)
#         q2 = question('python is easy','N')
#         self.__class__.questions.append(q2)
#         q3 = question('a cow can fly','N')
#         self.__class__.questions.append(q3)
#         q4 = question('a pig can fly','N')
#         self.__class__.questions.append(q4)
#         q5 = question('a chicken can fly','N')
#         self.__class__.questions.append(q5)
#     def set_points(self):
#         self.points += 1
#     def get_points(self):
#         return self.points
#     def get_question(self):
#         num =random.randint(0,4)
#         return self.__class__.questions[num]
#     def check_ans(self,pans):
#         gameans = self.get_question()
#         if gameans.ans == pans:
#             self.set_points()
#         else:
#             print('wrong ans the right ans is {}'.format(gameans.ans))
#
# p = quiz()
# while True:
#     print(p.get_points())
#     print(p.get_question().qus)
#     a = input('your ans:')
#     p.check_ans(a.upper())
#     y_n = input('continue y/n')
#     if y_n == 'y':
#         continue
#     else:
#         break





# class quiz:
#     questions = []
#     def __init__(self):
#         self.create_question()
#     def create_question(self):
#         q1 = question('can bird fly','N')
#         q2 = question('python is easy','N')
#         q3 = question('a cow can fly','N')
#         q4 = question('a pig can fly','N')
#         q5 = question('a chicken can fly','N')