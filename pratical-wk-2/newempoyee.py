from Employee import Empolyee

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