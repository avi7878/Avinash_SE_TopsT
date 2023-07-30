
counsellor_display = """

                                                WELCOME COUNSELLOR

                                                1) ADD STUDENT

                                                2) REMOVE STUDENT

                                                3) VIWE ALL STUDENT

                                                4) VIWE SPECIFIC STUDEN
"""
student_main = {}
global student_subject
global student_marks
global student_details

def fn_counselloer():
    
    counsellor_status = True
    while counsellor_status : 
        
        print(counsellor_display)    
        counsellor_role = int(input("Select Operation : "))
        student_details = {}

        match counsellor_role:
            
            case 1:
                rollno = int(input("Enter Roll No. : "  ))

                if rollno in student_main :
                    print("Roll No. Already Exist")
                
                else:
                    student_subject = {}

                    print("Roll No. Available for Register ")

                    fname = input("Enter First Name : ").upper()
                    lname = input("Enter Last Name : ").upper()
                    contact = int(input("Enter Contact No. : "))
                    student_details['fname'] = fname
                    student_details['lname'] = lname
                    student_details['contact'] = contact
                    
                    add_subject = True
                    while add_subject:
                        
                        student_marks={}

                        subject = input("Enter Subject Name : ").upper()
                        marks = int(input("Enter Marks : "))
                        fees = int(input("Enter Fees : "))
                        
                        student_marks['marks'] = marks
                        student_marks['fees'] = fees
                        
                        student_subject[subject]=student_marks
                        student_details['subject'] = student_subject

                        check = input("Add More Subjects (y/n) : ").upper()
                        if check == "Y":
                            add_subject = True
                        elif check == "N":
                            add_subject = False
                        else:
                            print("Enter Valid Input")
                            
                    faculty = input("Enter Faculty Name : ").upper()
                    student_details['faculty'] = faculty
                            
                    student_main[rollno] = student_details
                    print("Student Registration Succsefully Completed :)")
                    print(student_main)
                    

            case 2 :
                rollno = int(input("Enter Roll No. : "  ))

                if rollno in student_main :

                    print("Please Confirm Details Before Delete")
                    Viwedata = student_main.get(rollno)
                    print(Viwedata)
                    student_main.pop(rollno)
                    input()
                    print("Student Remove Successfully")
                
                else:
                    print("Roll No. Does Not Exist")
                
            case 3 :
                print(student_main)

            case 4:

                rollno = int(input("Enter Roll No. : "  ))

                if rollno in student_main :
                    
                    Viwedata = student_main.get(rollno)
                    print(Viwedata)
                
                else:
                    print("Roll No. Does Not Exist")

            case _:
                print("Enter Valid Input")
        

        check = input("Perform More Operaion (y/n) : ").upper()
        if check == "Y":
            counsellor_status = True
        elif check == "N":
            counsellor_status = False
        else:
            print("Enter Valid Input")