'''
	centering the menu'
'''
from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*73)    
    print("       MAIN MENU        ".center(73," "))
    print(" -----------------------".center(73," "))
    print(" 1. ADD STUDENT         ".center(73," "))
    print(" 2. FIND STUDENT        ".center(73," "))
    print(" 3. DELETE STUDENT      ".center(73," "))
    print(" 4. UPDATE STUDENT      ".center(73," "))
    print(" 5. DISPLAY ALL STUDENT ".center(73," "))
    print(" 0. QUIT/END            ".center(73," "))
    print(" -----------------------".center(73," "))
    #for i in range(1,5):print(" "*73)
    
def addstudent()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print("      Add Student     ".center(73))
    print("----------------------".center(73))

    #ID number validation
    while True:
        print(" "*25, end="")
        idno:str = input("IDNO      :   ").strip()
        if not idno:
            print(" "*25 + "ID number cannot be empty.")
        elif not idno.isdigit():
            print(" "*25 + "ID number must be numeric.")
        else:
            break

    #lastname validation
    while True:
        print(" "*25,end="")
        lastname:str = input("LASTNAME  :").strip()
        if not lastname:
            print(" "*25 + "Lastname cannot be empty")
        elif not lastname.isalpha():
            print("Lastname must be letters.")
        else:
            break

    #firstname validation
    while True:
        print(" "*25,end="")
        firstname:str = input("FIRSTNAME :").strip()
        if not firstname:
            print(" "*25 + "Firstname cannot be empty.")
        elif not firstname.isalpha():
            print(" "*25 + "Firstname must be letters.")
        else:
            break

    #course validation
    while True:
        print(" "*25,end="")
        course:str = input("COURSE    :").strip()
        if not course:
            print(" "*25 + "Course cannot be empty.")
        else:
            break

    #year level validation
    while True:
        print(" "*25,end="")
        level:str = input("LEVEL     :").strip()
        if not level:
            print(" "*25 + "Level cannot be empty.")
        break

    #save
    ok:bool = slist.addstudent(Student(idno,lastname,firstname,course,level))
    print("")
    print(" "*25, end="")
    if ok:
        print("Student added successfully.")

def findstudent()->None:
    system('cls')   
    for i in range(1,5):print(" "*73) 
    print(" "*25, end="")
    idno = input("Enter id number to search: ")
    student = slist.findstudent(idno)
    system('cls')
    print(" "*25, end="")
    if student != None:
        for i in range(1,5):print(" "*73) 
        print("Student Detail".center(73))
        print("----------------------".center(73))
        print("\n")
        print(" "*25,end="")
        print(f"ID number: {student.getidno()}")
        print(" "*25,end="")
        print(f"Name     : {student.getlastname()}, {student.getfirstname()}") 
        print(" "*25,end="")
        print(f"Course   : {student.getcourse()}")
        print(" "*25,end="") 
        print(f"Level    : {student.getlevel()}")
    else:
        for i in range(1,5):print(" "*73) 
        print("Student not found.".center(73))

def deletestudent()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print(" "*25, end="")
    idno = input("Enter id number to delete: ")
    ok = slist.deletestudent(idno)
    if ok:
        for i in range(1,5):print(" "*73)
        print("Student deleted successfully.".center(73))
    else:
        for i in range(1,5):print(" "*73)
        print("Student not found.".center(73))

def updatestudent()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print(" "*25, end="")
    idno = input("Enter id number to update: ")
    student = slist.findstudent(idno)
    if student is None:
        for i in range(1,5):print(" "*73)
        print("Student not found.".center(73))
        return

    system('cls')
    for i in range(1,5):print(" "*73)
    print("Enter new details".center(73))
    print("----------------------".center(73))
    print(" "*25, end="")
    lastname = input(f"LASTNAME ({student.getlastname()})   : ") 
    print(" "*25, end="")
    firstname = input(f"FIRSTNAME ({student.getfirstname()}): ")
    print(" "*25, end="")
    course = input(f"COURSE ({student.getcourse()})         : ")
    print(" "*25, end="")
    level = input(f"LEVEL ({student.getlevel()})            : ")

    updated_student = Student(idno, lastname, firstname, course, level)
    ok =slist.updatestudent(updated_student)
    if ok:
        for i in range(1,5):print(" "*73)
        print("Student updated successfully.".center(73))
    else:
        for i in range(1,5):print(" "*73)
        print("Update failed.".center(73))

def displayall()->None:
    system('cls')
    for i in range(1,5):print(" "*73)
    print("Students".center(73))
    print("----------------------".center(73))
    print("\n")
    slist.showlist()

def main()->None:
    
    option:str = ""
    while option !="0":
        displaymenu()
        print(" "*25,end="")
        option=input("Enter Option(0..5):  ")
        match option:
            case "1": addstudent()
            case "2": findstudent()
            case "3": deletestudent()
            case "4": updatestudent()
            case "5": displayall()
            case "0": print(" "*25 + "Program Ended")
            case   _: print("Invalid Option".center(120))
        print(" "*25,end="")
        print(end="")
        input(" "*25 + "\npress any key to continue...")
            
if __name__=="__main__":
    main()