#class Pet:
#    def __init__(self,name,typeo,age):
#        self.__name = name
#        self.__animal_type = typeo
#        self.__age = age
#    def set_name(self,name):
#        self.__name = name
#    def set_typeo(self,typeo):
#        self.__animal_type = typeo
#    def set_age(self):
#        self.__age = age
#    def get_name(self):
#        return self.__name 
#    def get_typeo(self):
#        return self.__animal_type 
#    def get_age(self):
#        return self.__age 
#Name = input("enter pet name")
#animal_type = input("enter pet type") 
#age = int(input("enter pet age "))
#p = Pet(Name,animal_type,age)
#print("pet",p.get_name(),'is a',p.get_typeo(),"and it is ",p.get_age(),'years old')







class customer:
    def __init__(self,customer_id,name):
        self.__customer_id = ""
        self.set_customer_id(customer_id)
        self.__name = name
    def set_customer_id(self,customer_id):
        if len(customer_id) == 5:
            if customer_id[-1].isalpha() and customer_id[0:4].isdigit():
                self.__customer_id = customer_id
        else:
            self.__customer_id = "invalid id"
    def set_name(self,name):
        self.__name = name
    def get_customer_id(self):
        return self.__customer_id
    def get_name(self):
        return self.__name 
    def display_details(self):
        print('===== customer details =====')
        print('customrr id:', self.__customer_id)
        print('customer name:',self.__name)






#cusid = input('input id')
#name = input('input name')
#customer1 = customer(cusid,name)
#customer1.display_details()

#class BankAccount:
#    def __init__(self,accountnumber,account_balance):
#        self.__accountnumber = accountnumber
#    def get_accountnumber(self):
#         if self.__accountnumber[0] == '1' or '0':
#            if self.__accountnumber[2] and self.__accountnumber[8] == '-':
#                return self.__accountnumber
#         else:
#            print('invalid bank account number')
#    def accountbalance(self,account_balance):
#        self.__accountbalance = account_balance
#    def get_accountbalance(self):
#        return self.__accountbalance
#    def get_interest_rate(self):
#        if self.__accountnumber[0] == '0':
#            self.__interst = 0.005
#            return self.__interst
#        else:
#            self.__interst = 0.01
#            return self.__interst
#    def deposit(self,deopsitamt):
#         self.__accountbalance += deopsitamt
#    def widthdraw(self,withdrawamt):
#        if withdrawamt > self.__accountbalance:
#            print('You have insufficient amount to withdraw')
#        else:
#         self.__accountbalance -= withdrawamt
#    def get_interest(self):
#        return self.__accountbalance * self.__interst
#
#accnum = input("enter account number")
#deopsit = int(input('enter deposit'))
#acc1 = BankAccount(accnum)
#acc1.accountbalance(deopsit)
#withdraw = int(input('enter withdraw'))
#acc1.widthdraw(withdraw)
#print(acc1.get_accountbalance())
#print(acc1.get_interest_rate())
#print(acc1.get_interest())
#
#














