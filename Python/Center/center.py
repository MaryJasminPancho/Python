'''
	centering the menu'
'''
from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*168)    
    print("       MAIN MENU        ".center(168," "))
    print(" -----------------------".center(168," "))
    print(" 1. ADD STUDENT         ".center(168," "))
    print(" 2. FIND STUDENT        ".center(168," "))
    print(" 3. DELETE STUDENT      ".center(168," "))
    print(" 4. UPDATE STUDENT      ".center(168," "))
    print(" 5. DISPLAY ALL STUDENT ".center(168," "))
    print(" 0. QUIT/END            ".center(168," "))
    print(" -----------------------".center(168," "))
    #for i in range(1,5):print(" "*73)
    
def addstudent()->None:
    system('cls')
    for i in range(1,5):print(" "*168)
    print("      Add Student     ".center(168))
    print("----------------------".center(168))

    #ID number validation
    while True:
        print(" "*78, end="")
        idno:str = input("IDNO      : ").strip()
        if not idno:
            print(" "*78 + "ID number cannot be empty.")
        elif not idno.isdigit():
            print(" "*78 + "ID number must be numeric.")
        else:
            break

    #lastname validation
    while True:
        print(" "*78,end="")
        lastname:str = input("LASTNAME  : ").strip()
        if not lastname:
            print(" "*78 + "Lastname cannot be empty")
        elif not lastname.isalpha():
            print(" "*78 + "Lastname must be letters.")
        else:
            break

    #firstname validation
    while True:
        print(" "*78,end="")
        firstname:str = input("FIRSTNAME : ").strip()
        if not firstname:
            print(" "*78 + "Firstname cannot be empty.")
        elif not firstname.isalpha():
            print(" "*78 + "Firstname must be letters.")
        else:
            break

    #course validation
    while True:
        print(" "*78,end="")
        course:str = input("COURSE    : ").strip()
        if not course:
            print(" "*78 + "Course cannot be empty.")
        else:
            break

    #year level validation
    while True:
        print(" "*78,end="")
        level:str = input("LEVEL     : ").strip()
        if not level:
            print(" "*78 + "Level cannot be empty.")
        break

    #save
    ok:bool = slist.addstudent(Student(idno,lastname,firstname,course,level))
    print("")
    print(" "*78, end="")
    if ok:
        print("Student added successfully.")

def findstudent()->None:
    system('cls')   
    for i in range(1,5):print(" "*168) 
    print(" "*78, end="")
    idno = input("Enter id number to search: ")
    student = slist.findstudent(idno)
    system('cls')
    print(" "*78, end="")
    if student != None:
        for i in range(1,5):print(" "*168) 
        print("Student Detail".center(168))
        print("----------------------".center(168))
        print("\n")
        print(" "*54,end="")
        print(f"ID number: {student.getidno()}")
        print(" "*54,end="")
        print(f"Name     : {student.getlastname()}, {student.getfirstname()}") 
        print(" "*54,end="")
        print(f"Course   : {student.getcourse()}")
        print(" "*54,end="") 
        print(f"Level    : {student.getlevel()}")
    else:
        for i in range(1,5):print(" "*168) 
        print("Student not found.".center(168))

def deletestudent()->None:
    system('cls')
    for i in range(1,5):print(" "*168)
    print(" "*25, end="")
    idno = input("Enter id number to delete: ")
    ok = slist.deletestudent(idno)
    if ok:
        for i in range(1,5):print(" "*168)
        print("Student deleted successfully.".center(168))
    else:
        for i in range(1,5):print(" "*168)
        print("Student not found.".center(168))

def updatestudent()->None:
    system('cls')
    for i in range(1,5):print(" "*168)
    print(" "*25, end="")
    idno = input("Enter id number to update: ")
    student = slist.findstudent(idno)
    if student is None:
        for i in range(1,5):print(" "*168)
        print("Student not found.".center(168))
        return

    system('cls')
    for i in range(1,5):print(" "*168)
    print("Enter new details".center(168))
    print("----------------------".center(168))
    print(" "*54, end="")
    lastname = input(f"LASTNAME ({student.getlastname()})   : ") 
    print(" "*54, end="")
    firstname = input(f"FIRSTNAME ({student.getfirstname()}): ")
    print(" "*54, end="")
    course = input(f"COURSE ({student.getcourse()})         : ")
    print(" "*54, end="")
    level = input(f"LEVEL ({student.getlevel()})            : ")

    updated_student = Student(idno, lastname, firstname, course, level)
    ok =slist.updatestudent(updated_student)
    if ok:
        for i in range(1,5):print(" "*168)
        print("Student updated successfully.".center(168))
    else:
        for i in range(1,5):print(" "*168)
        print("Update failed.".center(168))

def displayall()->None:
    system('cls')
    for i in range(1,5):print(" "*128)
    print("Students".center(128))
    print("----------------------".center(128))
    print("\n")
    slist.showlist()

def main()->None:
    
    option:str = ""
    while option !="0":
        displaymenu()
        print(" "*73,end="")
        option=input("Enter Option(0..5):  ")
        match option:
            case "1": addstudent()
            case "2": findstudent()
            case "3": deletestudent()
            case "4": updatestudent()
            case "5": displayall()
            case "0": print(" "*73 + "Program Ended")
            case   _: print("Invalid Option".center(168))
        print("\n")
        print(" "*46,end="")
        print(end="")
        input(" "*70 + "press any key to continue...")
            
if __name__=="__main__":
    main()