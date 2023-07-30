from counsellor_logic import *       
 
faculty_display = """

                                                WELCOME FACULTY

                                                1) ADD MARKS TO STUDENT

                                                2) VIWE ALL STUDENT
"""

def fn_faculty():
    frole = int(input("Select Roll : "))

    match frole:
        case 1 :            
            add_subject = True
            while add_subject:
                        
                student_marks={}

                subject = input("Enter Subject Name : ").upper()
                marks = int(input("Enter Marks : "))
                fees = int(input("Enter Fees : "))
                        
                student_marks['marks'] = marks
                student_marks['fees'] = fees

                student_main[student_subject[subject]]=student_marks
                student_main[student_details['subject']]=student_main[student_subject[subject]]

                # student_subject[subject]=student_marks
                # student_details['subject'] = student_subject

                check = input("Add More Subjects (y/n) : ").upper()
                if check == "Y":
                    add_subject = True
                elif check == "N":
                    add_subject = False
                else:
                    print("Enter Valid Input")
        case 2 :
            print(student_main)
        case _ :
            input("Enter Valid Input")