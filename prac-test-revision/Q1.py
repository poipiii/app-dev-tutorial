class Course:
    def __init__(self,course_code,course_name,intake_number):
        self.__course_code = self.set_course_code(course_code)
        self.__course_name = course_name
        self.__intake_number = intake_number
    def set_course_code(self,course_code):
        if len(course_code) == 6:
            self.__course_code = course_code
        else:
            self.__course_code = None

    def set_course_name(self,course_name):
        self.__course_name = course_name
    def set_intake_number(self,intake_number):
        self.__intake_number = intake_number
    def get_course_code(self):
        return self.__course_code
    def get_course_name(self):
        return self.__course_name
    def get_intake_number(self):
        return self.__intake_number
    def __str__(self):
        if self.__course_code is None:
            return 'invalid course code'
        else:
            return "the student intake for {}({}) is {}".format(self.__course_name,self.__course_code,self.__intake_number)
c1 = Course('ITDF0D','Diploma in Financial Informatics',70)
print(c1)




















# class course:
#     def __init__(self,course_code,course_name,intake_number):
#         self.__course_code = course_code
#         self.__course_name = course_name
#         self.__intake_number = intake_number
#
#     def set_course_name(self,course_name):
#         self.__course_name = course_name
#     def set_course_code(self,course_code):
#         self.__course_code = course_code
#     def set_intake_number(self,intake_number):
#         self.__intake_number = intake_number
#     def get_course_name(self):
#         return self.__course_name
#
#     def get_course_code(self):
#         return self.__course_code
#     def get_intake_number(self):
#         return self.__intake_number
#
#     def __str__(self):
#         return 'The student intake for {}({}) is {}'.format(self.__course_name,self.__course_code,self.__intake_number)
#
#
#
#
# c = course('ITDF08','Diploma in Financial Informatics','70')
#
# print(c)
#


# class Person:
#     def __init__(self, email, firstname, lastname):
#         self.email = email
#         self.firstname = firstname
#         self.lastname = lastname

#     def get_name(self):
#         return self.firstname + ' ' + self.lastname

# # Part (a) Create Instructor class, initializer and methods
# class student(Person):
#     def __init__(self,email,firstname,lastname):
#         super().__init__(email,firstname,lastname)
#         self.group = ''



# # Part (b) Create Student class, initializer
# class instructor(Person):
#     def __init__(self,email,firstname,lastname):
#         super().__init__(email,firstname,lastname)
#         self.students = {}
#     def get_name(self):
#         return self.firstname + ' ' + self.lastname +'(instructor)'

#     def add_student(self,student):
#         self.students[student] = student.email

# # Part (c) Implement load_students() Function
# def load_students():
#     s_list = []
#     try:
#         fw = open('prac-test-revision/student2.txt','r')
#         for i in fw:
#             line = i.rstrip('/n').replace(' ','').split(',')
#             s = student(line[2],line[0],line[1])
#             s_list.append(s)
#         fw.close()
#     except IOError:
#         print('file not found')
#     except:
#         print('unknown error')
#     return s_list

    
# # Part (c) Implement assign_students() Function
# def assign_students(instructor, group, class_size):
#     for i in class_size:
#         i.group = group
#         instructor.add_student(i)
#     print('{} students assigned to {}'.format(len(instructor.students),instructor.get_name()))

# # Test program
# group = 'PT01'
# instructor = instructor('may@gmail.com', 'May', 'Lim')
# students = load_students()
# assign_students(instructor, group, students)




















