class Question:
    Questionbank = {}
    answerbank = {}
    def __init__(self):
        self.__question = []
        self.__answer = []
    def set_Question(self,question):
        for i in self.__class__.Questionbank.keys():
            if i == question:
                self.__question.append(self.__class__.Questionbank[i])
            else:
                pass

    def set_Answer(self,answer):
        for i in self.__class__.answerbank.keys():
            if i == answer:
                self.__answer.append(self.__class__.answerbank[i])
            else:
                pass
    def get_Question(self):
        return self.__question
    
    def get_Answer(self):
        return self.__answer


class Quiz:
    def __init__(self):
        self.__playerans = []
        self.__playerscore = 0
    def Generate_num(self):
        import random 
        return random.randint(1,11)



testlist = []
for i in range():
    rand = Quiz()
    testlist.append(rand.Generate_num())
print(testlist)