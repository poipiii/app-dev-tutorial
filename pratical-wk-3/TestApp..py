'''
class Person:
    def __init__(self,name,nric):
        self.__name = name
        self.__nric = nric
    def set_name(self,name):
        self.__name = name
    def set_nric(self,nric):
        self.__nric = nric
    def get_name(self):
        return self.__name
    def get_nric(self):
        return self.__nric


class Student(Person):
    def __init__(self,name,nric,admin_no):
        super().__init__(name,nric)
        self.__admin_no = admin_no
        self.__test_mark = 0
        self.__exam_mark = 0
    def set_admin_no(self,admin_no):
        self.__admin_no = admin_no
    def set_test_mark(self,test_mark):
        self.__test_mark = test_mark
    def set_exam_mark(self,exam_mark):
        self.__exam_mark = exam_mark
    def get_admin_no(self):
        return self.__admin_no
    def get_test_mark(self):
        return self.__test_mark
    def get_exam_mark(self):
        return self.__exam_mark
    def computefinalmark(self):
        return (self.__exam_mark + self.__test_mark)/2
    #def __str__(self):
    #    return self.get_name() + ', admin no: ' + self.get_admin_no() + " final mark is: " + str(self.computefinalmark())

    
class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.__staff_id = staff_id
        self.__total_TeachingHour = 0
    def set_staff_id(self,staff_id):
        self.__staff_id = staff_id
    def set_total_teachingHour(self,total_teachingHour):
        self.__total_TeachingHour = total_teachingHour
    def get_staff_id(self):
        return self.__staff_id
    def get_total_teaching_hours(self):
        return self.__total_TeachingHour
    def computesalary(self):
        return self.__total_TeachingHour * 90
    #def __str__(self):
    #    return self.get_name() + ', staff id: ' + self.get_staff_id() + " earns: " + str(self.computesalary())


lec_name = input('enter lecture name')
lec_nric = input('lecture nric')
staff_id = input('enter staff id')
teach_hr = int(input('enter teaching hour'))
staff = Lecturer(lec_name,lec_nric,staff_id)
staff.set_total_teachingHour(teach_hr)
stu_name = input('enter student name')
stu_nric = input('student nric')
stu_id = input('enter admin no')
test_mark = int(input('enter test mark'))
exam_mark = int(input('enter exam mark'))
new_student = Student(stu_name,stu_nric,stu_id)
new_student.set_test_mark(test_mark)
new_student.set_exam_mark(exam_mark)
print(staff)
print(new_student)

'''
    
'''
class Person:
    def __init__(self,name,nric):
        self.__name = name
        self.__nric = nric
    def set_name(self,name):
        self.__name = name
    def set_nric(self,nric):
        self.__nric = nric
    def get_name(self):
        return self.__name
    def get_nric(self):
        return self.__nric


class Student(Person):
    def __init__(self,name,nric,admin_no):
        super().__init__(name,nric)
        self.__admin_no = admin_no
        self.__test_mark = 0
        self.__exam_mark = 0
    def set_admin_no(self,admin_no):
        self.__admin_no = admin_no
    def set_test_mark(self,test_mark):
        if test_mark < 100 and test_mark > 0:
            self.__test_mark = test_mark
        else:
            print("test mark is not valid")
    def set_exam_mark(self,exam_mark):
        if exam_mark > 100 and exam_mark < 0:
            self.__exam_mark = exam_mark
        else:
            print("exam mark is not valid")
    def get_admin_no(self):
        return self.__admin_no
    def get_test_mark(self):
        return self.__test_mark
    def get_exam_mark(self):
        return self.__exam_mark
    def computefinalmark(self):
        return (self.__exam_mark + self.__test_mark)/2
    def __str__(self):
        return self.get_name() + ', admin no: ' + self.get_admin_no() + " final mark is: " + str(self.computefinalmark())

    
class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.set_staff_id(staff_id)
        self.__total_TeachingHour = 0
    def set_staff_id(self,staff_id):
        if staff_id == self.get_nric():
            self.__staff_id = staff_id
        else:
            print('staff id and nric do not match ')
    def set_total_teachingHour(self,total_teachingHour):
        self.__total_TeachingHour = total_teachingHour
    def get_staff_id(self):
        return self.__staff_id
    def get_total_teaching_hours(self):
        return self.__total_TeachingHour
    def computesalary(self):
        return self.__total_TeachingHour * 90
    def __str__(self):
        return self.get_name() + ', staff id: ' + self.get_staff_id() + " earns: " + str(self.computesalary())


lec_name = input('enter lecture name')
lec_nric = input('lecture nric')
staff_id = input('enter staff id')
teach_hr = int(input('enter teaching hour'))
staff = Lecturer(lec_name,lec_nric,staff_id)
staff.set_total_teachingHour(teach_hr)
stu_name = input('enter student name')
stu_nric = input('student nric')
stu_id = input('enter admin no')
test_mark = int(input('enter test mark'))
exam_mark = int(input('enter exam mark'))
new_student = Student(stu_name,stu_nric,stu_id)
new_student.set_test_mark(test_mark)
new_student.set_exam_mark(exam_mark)
print(staff)
print(new_student)
'''

#class Fish:
#    def __init__(self, first_name, last_name="Fish"):
#        self.first_name = first_name
#        self.last_name = last_name
#    def swim(self):
#        print("The fish is swimming.")
#    def swim_backwards(self):
#        print("The fish can swim backwards.")
#
##clown fish will inherit all the methods
#
#class ClownFish(Fish):
#    def lives_in_sea(self):
#        print("The clown fish lives in the sea")
#



class Player:
    def __init__(self,name):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name



#QN 3
class Basketballplayer(Player):
    postitions = ['Guard', 'Forward','Center']
    player_pos = {}
    def __init__(self,name,position):
        super().__init__(name)
        self.set_position(position)
    def set_position(self,position):
        if position in self.__class__.postitions:
            self.__position = position
            self.__class__.player_pos[self.get_name()] = position
        else:
            return 'invalid position'
    def get_position(self):
        return self.__position
    
    
team_name = input('Enter the basketball team name ')
for i in Basketballplayer.postitions:
    player_postition = input('which player is playing as a %s'%i)
    Basketballplayer(player_postition,i)
for x in Basketballplayer.player_pos:
    print(x,' is playing as ',Basketballplayer.player_pos[x])
