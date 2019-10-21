##class user:
##    def __init__(self,firstname,lastname):
##        self.firstname = firstname
##        self.lastname = lastname
##    def get_full_name(self):
##        return self.firstname +" "+ self.lastname
##
##
##user1 = user("john","lee")
##print(user1.get_full_name())
#
#
#
#
#class person:
#    def set_weight(self,weight):
#        self.__weight = weight
#
#    def set_height(self,height):
#       self.__height = height
#    def get_weight(self,weight):
#        return self.__weight 
#    def get_height(self,height):
#        return self.__height 
#    def get_bmi(self):
#        return  self.__weight / self.__height ** 2
#
#
#usrlist = []
#for x in range(3):
#    height = float(input("enter height of person"+str(x+1)))
#    weight = float(input("enter height of person"+str()))
#    p = person()
#    p.set_height(height)
#    p.set_weight(weight)
#    usrlist.append(p)
#
#
#print(p.get_bmi for p in usrlist)

class Bank_account:
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount > self.__balance:
            print("balance not enought")
        else:
            self.__balance -= amount

b = Bank_account()
b.deposit(5000)
b.withdraw(6000)
print(b.get_balance())












