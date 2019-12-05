import Person

class Lecturer(Person.Person):
    def __init__(self, name, nric, staff_id, totalteachinghr):
        #Person.Person.__init__(self, name, nric)
        super().set_name(name)
        super().set_nric(nric)
        #self.__staff_Id = staff_id
        self.__staff_Id = ""
        self.set_staff_id(staff_id)

        self.__total_TeachingHour = totalteachinghr

    def get_staff_id(self):
        return self.__staff_Id
    def get_total_teachinghour(self):
        return self.__total_TeachingHour
    def set_staff_id(self, staff_id):
        if self.get_nric() == staff_id:
            self.__staff_Id = staff_id
        else:
            print("Not the same")

    def set_total_teachinghour(self, totalteachinghr):
        self.__total_TeachingHour = totalteachinghr

    def computeSalary(self):
        return self.__total_TeachingHour*90
