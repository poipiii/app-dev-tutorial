# class Player:
#     def __init__(self,player_name):
#         self.__player_name =player_name
#     def set_name(self,player_name):
#         self.__player_name =player_name
#     def get_name(self):
#         return self.__player_name
#
# class BasketballPlayer(Player):
#     positions = ['Guard','Forward','Center']
#     def __init__(self, name, position):
#         super().__init__(name)
#         self.__position = ''
#         self.set_pos(position)
#     def set_pos(self, position):
#         if position in self.__class__.positions:
#             self.__position = position
#         else:
#             return 'invalid position'
#     def get_pos(self):
#         return self.__position
#
#
# plist = []
# for i in range(3):
#     player = input('enter playername')
#     pos = input(('enter player position'))
#     p = BasketballPlayer(player,pos)
#     plist.append(p)
#
# for i in plist:
#     print('{} is playing as {}'.format(i.get_name(),i.get_pos()))


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
        self.set_exam_mark(exam_mark)
    def set_admin_no(self,admin_no):
        self.__admin_no = admin_no
    def set_test_mark(self,test_mark):
        self.__test_mark = test_mark
    def set_exam_mark(self,exam_mark):
        if  exam_mark >=0 and exam_mark <= 100:
            self.__exam_mark = exam_mark
        else:
            self.__exam_mark = False
    def get_test_mark(self):
        return self.__test_mark
    def get_exam_mark(self):
        return self.__exam_mark
    def get_admin_no(self):
        return self.__admin_no

    def compute_final_mark(self):
        return (self.__test_mark + self.__exam_mark) / 2

    def __str__(self):
        if self.__exam_mark is False:
            return 'invalid exam mark'
        else:
            return '{},{},{}'.format(s.get_name(),s.get_admin_no(),s.compute_final_mark())

class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.set_staff_id(staff_id)
        self.__total_teaching_hour = 0
    def set_staff_id(self,staff_id):
        if staff_id == self.get_nric():
            self.__staff_id = staff_id
        else:
            self.__staff_id = False
    def set_total_teaching_hour(self,teaching_hour):
        self.__total_teaching_hour = teaching_hour
    def get_staff_id(self):
        return self.__staff_id
    def get_total_teaching_hour(self):
        return self.__total_teaching_hour
    def computeslalry(self):
        return self.__total_teaching_hour * 90
    def __str__(self):
        if self.__staff_id is False:
            return 'nric and staff id are not the same'
        else:
            return '{},{},{}'.format(l.get_name(),l.get_staff_id(),l.computeslalry())








lec_n = input('enter lecture name')
lec_nric = input('enter lecturer nric')
lec_staff_id = input('enter staff id')
teach_hr = int(input('enter total teaching hour'))
stu_name = input('student name')
stu_nric = input('enter student nric')
stu_admin_no = input('enter student admin no')
test_mark = int(input('enter test mark'))
exam_mark = int(input('enter exam mark'))
l =Lecturer(lec_n,lec_nric,lec_staff_id)
l.set_total_teaching_hour(80)
s = Student(stu_name,stu_nric,stu_admin_no)
s.set_test_mark(test_mark)
s.set_exam_mark(exam_mark)

print('{},{},{}'.format(s.get_name(),s.get_admin_no(),s.compute_final_mark()))
