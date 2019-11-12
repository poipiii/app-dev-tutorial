#try:
#    count = int(input('How many number you want to capture?'))
#    numList = []
#    for i in range(count):
#        msg = 'Enter number #' + str(i+1)
#        num = int(input(msg))
#        numList.append(num)
#    print('The lowest number in the list:', min(numList))
#    print('The highest number in the list:', max(numList))
#    print('The total of the number in the list:', sum(numList))
#    print('The average of the number in the list:',sum(numList)/len(numList))
#except ValueError:
#    print('there is a value error')
#except ZeroDivisionError:
#    print('there is a zerodivison error')
#except:
#    print('there is a unknown error')

class Student:
    def __init__(self, name):
       self.name = name
       self.math = 0
       self.chinese = 0
       self.english = 0
       self.science = 0
       self.choices = []
       self.allocation = ''
    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4
    def __str__(self):
        return "{} scores {},allocation is {}, the choices are {} ,{}, {}".format(self.name,self.get_score(),self.allocation,self.choices[0],self.choices[1],self.choices[2])

def by_score(student_obj):
    return student_obj.get_score()      
def main():
    students = load_result()
    students = sorted(students, key=by_score, reverse = True)
    for s in students:
        s.choices.append('SchoolA')
        s.choices.append('SchoolB')
        s.choices.append('SchoolC')
    school_vac ={'SchoolA':5,'SchoolB':5,'SchoolC':5}
    for s in students:
        for c in s.choices:
            if school_vac.get(c) > 0:
                s.allocation = c
                school_vac[c] -= 1
                break
    for s in students:
       print(s)
    
def load_result():
    students = []
    try:

        fw = open('C:/Users/Loy juncheng/Desktop/nyp sem 2/app dev/app-dev-turoial\pratical-wk-5/results.txt','r')

        for line in fw:
            alist = line.split(',')
            name =  alist[0]
            s = Student(name)
            s.math =  float(alist[1])
            s.chinese =  float(alist[2])
            s.english =  float(alist[3])
            s.science =  float(alist[4])
            students.append(s)
        fw.close()

    except IOError:
        print('file not found')
    return students

main()
