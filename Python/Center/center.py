'''
	centering the menu'
'''
from os import system
from studentlist import StudentList
from student import Student

slist = StudentList(10)

def displaymenu()->None:
    system('cls')
    for i in range(1,5):print(" "*97)    
    print("       MAIN MENU        ".center(97," "))
    print(" -----------------------".center(97," "))
    print(" 1. ADD STUDENT         ".center(97," "))
    print(" 2. FIND STUDENT        ".center(97," "))
    print(" 3. DELETE STUDENT      ".center(97," "))
    print(" 4. UPDATE STUDENT      ".center(97," "))
    print(" 5. DISPLAY ALL STUDENT ".center(97," "))
    print(" 0. QUIT/END            ".center(97," "))
    print(" -----------------------".center(97," "))
    #for i in range(1,5):print(" "*73)
    
def addstudent()->None:
    system('cls')
    for i in range(1,5):print(" "*97)
    print("Add Student           ".center(73))
    print("----------------------".center(73))
    print(" "*25,end="")
    idno:str = input("IDNO      :")
    print(" "*25,end="")
    lastname:str = input("LASTNAME  :")
    print(" "*25,end="")
    firstname:str = input("FIRSTNAME :")
    print(" "*25,end="")
    course:str = input("COURSE    :")
    print(" "*25,end="")
    level:str = input("LEVEL     :")
    ok:bool = slist.addstudent(Student(idno,lastname,firstname,course,level))

def findstudent()->None:
    system('cls')
    idno = input("Enter id number to search: ")
    student = slist.findstudent(idno)
    if student != None:
        print("Student found: ")
        print(f"{student.getidno()} \n{student.getlastname()}, {student.getfirstname()} \n{student.getcourse()} \n{student.getlevel()}")
    else:
        print("Student not found.")

def deletestudent()->None:
    system('cls')
    idno = input("Enter id number to delete: ")
    ok = slist.deletestudent(idno)
    if ok:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def updatestudent()->None:
    system('cls')
    idno = input("Enter id number to update: ")
    student = slist.findstudent(idno)
    if student is None:
        print("Student not found.")
        return

    print("Leave field blank to keep current value.")
    lastname = input(f"LASTNAME ({student.getlastname()}): ") 
    firstname = input(f"FIRSTNAME ({student.getfirstname()}): ")
    course = input(f"COURSE ({student.getcourse()}): ")
    level = input(f"LEVEL ({student.getlevel()}): ")

    updated_student = Student(idno, lastname, firstname, course, level)
    ok =slist.updatestudent(updated_student)
    if ok:
        print("Student updated successfully.")
    else:
        print("Update failed.")

def displayall()->None:
    system('cls')
    slist.showlist()
def main()->None:
    
    option:str = ""
    while option !="0":
        displaymenu()
        print(" "*40,end="")
        option=input(" Enter Option(0..5):   ")
        match option:
            case "1": addstudent()
            case "2": findstudent()
            case "3": deletestudent()
            case "4": updatestudent()
            case "5": displayall()
            case "0": print("Program Ended".center(73))
            case   _: print("Invalid Option".center(73))
        print(" "*75,end="")
        print(end="")
        input("press any key to continue...")
            
if __name__=="__main__":
    main()