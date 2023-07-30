from counsellor_logic import *
from faculty_logic import *
from student_logic import * 

welcome = """
                                                WELCOME TO STUDENT MANAGEMENT SYSTEM

                                                1) COUNSELLOR

                                                2) FACULTY

                                                3) STUDENT
"""

status = True
while status :
    
    print(welcome)
    role = int(input("Select Role By Entering Role : "))
    
    match role:

        case 1:         
            print(counsellor_display)
            fn_counselloer()

        case 2:
            print(faculty_display)
            fn_faculty()

        case 3 :
            print(student_display)  
            fn_student()
        case _:
            print("Enter Valid Input")


    check = input("Want to Exit (y/n) : ").upper()
    if check == "Y":
        status = False
    elif check == "N":
        status = True
    else:
        print("Enter Valid Input")