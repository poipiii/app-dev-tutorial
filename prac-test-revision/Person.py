class Person:
    def __init__(self, email, firstname, lastname):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return self.firstname + ' ' + self.lastname

# Part (a) Create Instructor class, initializer and methods
class Instructor(Person):
    def __init__(self,email,firstname,lastname):
        super().__init__(email,firstname,lastname)
        self.students = {}
    def get_name(self):
        return self.firstname + ' ' + self.lastname +'(instructor)'
    def add_student(self,student):
        self.students[student] = student.email

# Part (b) Create Student class, initializer
class Student(Person):
   def __init__(self,email,firstname,lastname):
        super().__init__(email,firstname,lastname)
        self.group = ''


# Part (c) Implement load_students() Function
def load_students():
    stu = []
    try:
        file = open('prac-test-revision/student.txt','r')
        for line in file:
            split = line.rstrip('\n').split(',')
            firstname = split[0] 
            lastname = split[1] 
            email = split[2] 
            s = Student(email,firstname,lastname)
            stu.append(s)
        file.close()
    except IOError:
        print('file not found')
    except:
        ('unkmown error')
    return(stu)
# Part (c) Implement assign_students() Function
def assign_students(instructor, group, class_size):
    for i in class_size:
        instructor.add_student(i)
    print("{} student assigned to {}".format(len(instructor.students),instructor.get_name()))
# Test program
group = 'PT01'
instructor = Instructor('may@gmail.com', 'May', 'Lim')
students = load_students()
assign_students(instructor,group,students)

