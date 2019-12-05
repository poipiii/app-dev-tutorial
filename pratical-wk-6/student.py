import shelve
class Student:
    def __init__(self,stu_id,name,gpa):
        self.id = stu_id
        self.name = name
        self.gpa = gpa
    #setters
    def set_id(self,id):
        self.id = id

    def set_name(self,name):
       self.name = name

    def set_gpa(self,gpa):
        self.gpa = gpa
    #getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gpa(self):
       return self.gpa

def write_db(student_obj):
    db = shelve.open("student.db","c")
    if str(student_obj.id) not in db:
        db[str(student_obj.id)] = student_obj
        print('print student record added')
        db.close()
    else:
        print('ERROR: id already exist')
def read_db():
    student_list = []
    db = shelve.open("student.db","c")
    for stu_id in db:
        s = db[stu_id]
        student_list.append(s)

    for stu in student_list:
        print(stu.id,stu.name,stu.gpa)
    db.close()

def modify_db(stu_id,new_name):
    db = shelve.open('student.db',"c")
    if stu_id in db:
        s = db[stu_id]
        s.name = new_name
        db[stu_id] = s
    else:
        print('no such id')
    db.close()

def del_db(stu_id):
    db = shelve.open('student.db',"c")
    if stu_id in db:
        del(db[stu_id])
    else:
        print('no such id')
    db.close()
def display():
    print('''==== student records=====
    1.add student
    2.display all student
    3.update student record
    4.delete student record
    Q.quit''')
while True:
    display()
    option = input('please enter an option')
    if option == '1':
        print('==== ADD ====')
        stu_id = int(input('input student id: '))
        stu_name = input('input student name: ')
        stu_gpa = float(input('input student gpa'))
        stu = Student(stu_id,stu_gpa,stu_name)
        write_db(stu)

    if option == '2':
        print('==== DISPLAY ====')
        read_db()

    if option == '3':
        print('==== MODIFY ====')
        c_stu_id = int(input('input student id: '))
        new_stu_name = input('input new student name: ')
        modify_db(c_stu_id,new_stu_name)

    if option == '4':
       print('==== DELETE ====')
       D_stu_id = int(input('input student id: '))
       del_db(D_stu_id)

    if option.lower() == 'q':
        break

# import shelve

# class student:
#     def __init__(self,id,name,gpa):
#         self.__id = id
#         self.__name = name
#         self.__gpa = gpa
#     def set_id(self,id):
#         self.__id = id
#     def set_name(self,name):
#         self.__name = name
#     def set_gpa(self,gpa):
#         self.__gpa = gpa
#     def get_id(self):
#         return self.__id
#     def get_name(self):
#         return self.__name
#     def get_gpa(self):
#         return self.__gpa

# def add_shelve(sid,name,gpa):
#         fw = shelve.open('student.db','c')
#         if str(sid) not in fw:
#             s = student(str(sid),name,gpa)
#             fw[s.get_id()] = s
#         else:
#             print('error already exits')
#         fw.close()
# def del_shelve(id_del):
#         fw =shelve.open('student.db','c')
#         if id_del in fw:
#             del(fw[id_del])
#         fw.close()
# def modify_shelve(sid,name,gpa):
#         fw =shelve.open('student.db','c')
#         if sid in fw:
#             s = fw[sid]
#             s.set_name(name)
#         fw.close()
# def display():
#     fw =shelve.open('student.db','c')
#     for i in fw:
#         print('{},    {},     {}'.format(fw[i].get_id(),fw[i].get_name,fw[i].get_gpa()))
#     fw.close()
























