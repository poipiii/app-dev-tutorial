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
#import random
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
#def count():
#    usr_file = open('usr_text.txt','r')
#    test = usr_file.readlines()
#    print(test)

#name = input('input name')
#weight = float(input('input weight'))
#height = float(input('input height'))
#files()
#count()
#test = [random.randint(1,999) for i in range(10)]
#print(test)


# class Student:
#  def __init__(self, name):
#     self.name = name
#     self.math = 0
#     self.chinese = 0
#     self.english = 0
#     self.science = 0
#     self.choices = []
#     self.allocation = ''
#  def get_score(self):
#      return (self.math + self.chinese + self.english + self.science) / 4
#
# def sort_s(student):
#     return student.get_score()
# def main():
#     choice = {'SchoolA':5,'SchoolB':5,'SchoolC':5}
#     students = load_result()
#     students= sorted(students, key=sort_s, reverse=True)
#     for s in students:
#         s.choices.append('SchoolA')
#         s.choices.append('SchoolB')
#         s.choices.append('SchoolC')
#
#     for s in students:
#         for c in choice:
#             if choice[c] > 0:
#                 s.allocation = c
#                 choice[c] -= 1
#                 break
#
#     for s in students:
#         print('{} scores {}, allocation:{} the choices are {}, {}, {}'.format(s.name, s.get_score(),s.allocation,s.choices[0],s.choices[1],s.choices[2]))
# def load_result():
#     students = []
#     try:
#         fw = open('results.txt','r')
#     except IOError:
#
#         print('invalid file or file could not be found')
#
#     else:
#         for i in fw:
#             line = i.rstrip('\n').split(',')
#             s = Student(line[0])
#             s.math = int(line[1])
#             s.chinese = int(line[2])
#             s.english = int(line[3])
#             s.science = int(line[4])
#             students.append(s)
#         fw.close()
#     return students
# main()



