#class Module():
#    def __init__(self,Id,name,hours):
#        self.__id = Id
#        self.__name = name
#        self.__hours = hours
#    def set_id(self,Id):
#        self.__id = Id
#    def set_name(self,name):
#        self.__name = name
#    def set_hours(self,hours):
#        self.__id = hours
#    def get_id(self):
#        return self.__id
#    def get_name(self):
#        return self.__name
#    def get_hours(self):
#        return self.__hours 
#    def __str__(self):
#        return "The modeule hours for {} ({}) is {} hours".format(self.get_name(),self.get_id(),self.get_hours())
#
#c = Module('IT1111','PROG ESS',60)
#print(c)


class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name =last_name

    def get_name(self):
        return self.first_name +' '+ self.last_name
    
class Student(Person):
    def __init__(self,first_name,last_name,group):
      super().__init__(first_name,last_name)
      self.group = group

    def get_name(self):
        return self.first_name +' '+ self.last_name + '-' +self.group

class Tutor(Person):
    def __init__(self,first_name,last_name,contact):
      super().__init__(first_name,last_name)
      self.contact = contact

    def get_name(self):
        return self.first_name +' '+ self.last_name + 'x'+self.contact
        
Student_list = ['John,Lim,IT1901','Max ,Tang,IT1901','Jeff,Ting,IT1902']   

def convert_to_list(student_str_list):
    obj_list = []
    for i in student_str_list:
        students = i.split(',')
        first_name = students[0]
        last_name = students[1]
        group = students[2]

        s = Student(first_name,last_name,group)
        obj_list.append(s)
    return obj_list




def parse_list(list):
    obj_list = []
    for i in list:
        x = i.rstrip('\n').replace(' ','').split(',')
        print(x)
        if 'Student' in x:
            s_first_name = x[0]
            s_last_name = x[1]
            group = x[2]
            s = Student(s_first_name,s_last_name,group)
            obj_list.append(s)
        elif 'Tutor' in x:
            t_first_name = x[0]
            t_last_name = x[1]
            contact = x[2]
            t = Tutor(t_first_name,t_last_name,contact)
            obj_list.append(t)
        else:
            p_first_name = x[0]
            p_last_name = x[1]
            p = Person(p_first_name,p_last_name)
            obj_list.append(p)
    return obj_list



def get_record():
    rec_list = []
    f = open('prac-test-revision/student.txt','r')
    for i in f:
        rec_list.append(i)
    f.close()
    return rec_list
list_1 = [ 'John, Lim, 1600,Tutor', 'James, Toh, 01,Student', 'Max, Tang, IT1901, Student','Jen, Lee, IT1901, Student', 'Jane, Teng, 1700, Tutor', 'Jon, Tong, Person ', 'Danny, Tan, Person', 'Elvin, Ong, IT1901, Student', 'Adrian, Chua, 1800, Tutor ', 'Jeff, Ting, IT1902, Student']
test = get_record()
test_2 = parse_list(test)
for i in test_2:
    print(i.get_name())


