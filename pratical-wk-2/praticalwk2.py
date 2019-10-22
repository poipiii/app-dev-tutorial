class Empolyee:
    Empolyeedict={}
    def __init__(self,name,emid,department,title):
        self.__name = name
        self.__id = emid
        self.__department = department
        self.__title = title 
    #setters
    def set_name(self,name):
        self.__name = name
    def set_id(self,emid):
        self.__id = emid
    def set_department(self,department):
        self.__department = department
    def set_title(self,title):
        self.__title = title
    #getters
    def get_name(self,name):
        return self.__name 
    def get_id(self,emid):
        return self.__id 
    def get_department(self,department):
        return self.__department 
    def get_title(self,title):
        return self.__title 

        
    def addemployee(self):
        self.__class__.Empolyeedict[self.__id]={'name':self.__name,'department':self.__department,"title":self.__title}
    def get_empolyeefromdict(self,uuid):
        return("name:",self.__class__.Empolyeedict[uuid]['name'],"department:",self.__class__.Empolyeedict[uuid]['department'],"title:",self.__class__.Empolyeedict[uuid]['title'])
    def updateemployee(self,uuid,newname,newdepart,newtitle):
        self.__class__.Empolyeedict[uuid]['name'] = newname
        self.__class__.Empolyeedict[uuid]['department'] = newdepart
        self.__class__.Empolyeedict[uuid]['title'] = newtitle
    def delemployee(self,uuid):
         self.__class__.Empolyeedict.pop(uuid)
    #def get_empolyee(self):
    #    return("name:",self.__name,"id:",self.__id,"department:",self.__department,"title:",self.__title)


while True:
    print('''Select the program (1-5) to run:
    1. Search for an employee
    2. Add new employee
    3. Update employee details
    4. Delete and employee
    5. Quit the program
    ''')
    command  = int(input("Enter your command (1-5) :"))
    if command == 1:
        searchid = int(input("input id to search"))
        print(employ.get_empolyeefromdict(searchid))
        
    elif command == 2:
        name = input("enter your name ")
        emid = int(input("enter your id"))
        department = input("enter your department")
        title = input("enter your title")
        employ = Empolyee(name,emid,department,title)
        employ.addemployee()
        print(employ.Empolyeedict)
    elif command == 3:
        updateid = int(input("input id to update"))
        newname = input("enter your name ")
        newdepartment = input("enter your department")
        newtitle = input("enter your title")
        employ.updateemployee(updateid,newname,newdepartment,newtitle)
    
    elif command == 4:
        delid = int(input("input id to update"))
        employ.delemployee(delid)
    elif command == 5:
        break

    