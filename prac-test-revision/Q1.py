class Course:
    def __init__(self,course_code,course_name,intake_number):
        self.set_course_code(course_code)
        self.__course_name = course_name
        self.__intake_number = intake_number
    def set_course_code(self,course_code):
        self.__course_code = course_code
        if len(course_code) != 6:
             self.__course_code = ''
             print('invalid course code')
        else:
            pass

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
        return "the student intake for {}({}) is {}".format(self.__course_name,self.__course_code,self.__intake_number)



c1 = Course('ITDF0','Diploma in Financial Informatics',70)
print(c1)

