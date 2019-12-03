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

#class Bank_account:
#    def __init__(self):
#        self.__balance = 0
#    def get_balance(self):
#        return self.__balance
#    def deposit(self,amount):
#        self.__balance += amount
#    def withdraw(self,amount):
#        if amount > self.__balance:
#            print("balance not enought")
#        else:
#            self.__balance -= amount
#
#b = Bank_account()
#b.deposit(5000)
#b.withdraw(6000)
#print(b.get_balance())


# class customer:
#     def __init__(self,id,name):
#         self.__customer_id = ''
#         self.set_customer_id(id)
#         self.__name = name
#
#     def set_customer_id(self, id):
#         if len(id) == 6 and id[0:4].isdigit() and id[-1].isalpha():
#             self.__customer_id = id
#         else:
#             print('invalid id')
#     def set_name(self, name):
#         self.__name = name
#
#     def get_customer_id(self):
#         return self.__customer_id
#     def get_name(self):
#         return self.__name
#
#     def display_details(self):
#         print('''
#         ====customer details=====
#         Customer Id: {}
#         Customer Name: {}'''.format(self.get_customer_id(),self.get_name()))
#
#
# p1 = customer('12345A','nana poi')
# p1.display_details()



# class BankAccount:
#     def __init__(self,account_number):
#         self.__account_number = account_number
#         self.account_balance = 0
#     def get_accnum(self):
#         return self.__account_number
#     def get_accbalance(self):
#         return  self.account_balance
#     def deposit(self,amount):
#         self.account_balance = amount
#     def withdraw(self,amount):
#         if amount > self.get_accbalance():
#             print('insufficent balance')
#         else:
#             self.account_balance -= amount
#     def get_interst_rate(self):
#         if self.get_accnum()[0] == '1':
#             return   0.01
#         else:
#             return  0.005
#
#     def get_interst(self):
#         return self.get_accbalance() * self.get_interst_rate()
#
#
#
#
# b = BankAccount('10-12345-11')
# b.deposit(500)
# print(b.get_accbalance())
# b.withdraw(100)
# print(b.get_accnum())
# print(b.get_accbalance())
# print(b.get_interst_rate())
# print(b.get_interst())