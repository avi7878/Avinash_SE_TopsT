from counsellor_logic import *

student_display = """

                                                WELCOME STUDENT
"""

def fn_student():

    rollno = int(input("Enter Roll No. : "  ))

    if rollno in student_main :
                    
        Viwedata = student_main.get(rollno)
        print(Viwedata)

    else:
            print("Roll No. Does Not Exist")