#class Customer:
#    def __init__(self,name,address,mobile):
#        self.__name = name
#        self.__address = address
#        self.__mobile = mobile
#    def set_name(self,name):
#        self.__name = name
#    def set_address(self,address):
#        self.__address = address
#    def set_mobile(self,mobile):
#        self.__mobile = mobile
#   
#c = Customer('billy tan',"123 bishan lane","87231556")

#
#class phone:
#    count = 0
#    def __init__(self,number,owner):
#        self.__number = number        
#        self.__owner = owner
#        self.__class__.count +=1
#    def set_number(self,number):
#        self.__number = number
#    def set_owner(self,owner):
#        self.__number = owner
#    def get_number(self):
#        return self.__number
#    def get_owner(self):
#        return self.__owner
#    def increment(self):
#         self.__class__.count += 1
#
#
#def reset():
#    phone.count = 0
#p1 = phone('123456','john')
#p2 = phone('87654321','janice')
#reset()
#p1.increment()
#print(phone.count)



class Game:
    def __init__(self,playerName):
        self.__playerName = playerName
        self.__score = 0
    def set_score(self,score):
        self.__score = score
    def get_playerName(self):
        return self.__playerName
    def get_score(self):
        return self.__score
    def __str__(self):
        return self.__playerName +"'s score is " + str(self.__score)
    
p1 = Game('john Tee')
p2 = Game('Mary zee')
p1.set_score(100)
p2.set_score(192)
def findwinner(p1,p2):
    if p1.get_score() > p2.get_score():
         print(p1)
    elif p2.get_score() > p1.get_score():
         print(p2)
    else:
        pass


findwinner(p1,p2)