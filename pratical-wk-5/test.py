#class bmi:
#    def __init__(self,name,weight,height):
#        self.name = name
#        self.weight = weight
#        self.height = height
#    def files():
#        usr_file = open('usr_text.txt','w')
#        usr_file.write(self.name,self.weight,self.height)
#        usr_file.close()
#
#    def read_file():
#        usr_file = open('usr_text.txt')
#        usr_file.readline



#def files(name,weight,height):
#    info = [name,weight,height]
#    usr_file = open('usr_text.txt','w')
#    for i in info:
#        usr_file.write(str(i))
#    usr_file.close()
#def read_file():
#    usr_file = open('usr_text.txt')
#    usr_file.readline()
#
import random
#def files():
#    
#    usr_file = open('usr_text.txt','a')
#    for i in range(4):
#        num = random.randint(1,100)
#        usr_file.write(str(num)+'\n')
#    usr_file.close()

#def files():
#    
#    usr_file = open('usr_text.txt','a')
#    usr_file.write('100\n')
#    usr_file.write('100 \n')
#    usr_file.write('100 \n')
#    usr_file.close()
def count():
    usr_file = open('usr_text.txt','r')
    test = usr_file.readlines()
    print(test)

#name = input('input name')
#weight = float(input('input weight'))
#height = float(input('input height'))
#files()
count()
#test = [random.randint(1,999) for i in range(10)]
#print(test)