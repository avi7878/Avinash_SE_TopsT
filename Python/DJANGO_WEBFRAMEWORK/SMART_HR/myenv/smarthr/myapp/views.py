from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from random import *
from django.core.mail import send_mail
from django.contrib import messages


 
# Create your views here.

def home(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Hr":
            cid = Hr.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid                            
            }
            return render(request,'myapp/admin-dashboard.html',context)
        # return render(request,'myapp/admin-dashboard.html')
    else:
        return render(request,'myapp/login.html')
    
def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Hr":
            cid = Hr.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid                            
            }
            return render(request,'myapp/admin-dashboard.html',context)
        else:
            pass
    elif request.POST:
        print("Submit buttom hit")
        p_email = request.POST['email']
        p_password = request.POST['password']
        print("Email ======> ",p_email)
        try:
            uid = User.objects.get(email = p_email)
            if uid.password == p_password:
                if uid.role == "Hr":
                    cid = Hr.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    print(cid)
                    context = {
                        "uid" : uid,
                        "cid" : cid                            
                    }
                    return render(request,'myapp/admin-dashboard.html',context)
                else:
                    pass
            else:
                print("Wrong password")
                context = {
                    "e_msg" : "Invalid Password"
                }
                return render(request,'myapp/login.html',context)
        except:
            context = {
                "e_msg" : "Invalid Email or Password"
            }
            return render(request,'myapp/login.html',context)
    else:
        print("Only page refresh")
    return render(request,'myapp/login.html')

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")
    
def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Hr":
            cid = Hr.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid                            
            }
            return render(request,'myapp/profile.html',context)

def update_hr_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Hr":
            cid = Hr.objects.get(user_id = uid)

            cid.first_name = request.POST['first_name']
            cid.last_name = request.POST['last_name']
            cid.date_of_birth = request.POST['date_of_birth']
            # cid.converted_date = convert_date(cid.date_of_birth)
            # print("date ========> ",cid.converted_date)
            cid.address = request.POST['address']
            cid.gender = request.POST['gender']
            cid.state = request.POST['state']
            cid.country = request.POST['country']
            cid.pin_code = request.POST['pin_code']
            cid.contact_no = request.POST['contact_no']
            cid.nationality = request.POST['nationality']
            cid.religion = request.POST['religion']
            cid.marital_status = request.POST['marital_status']
            cid.no_of_children = request.POST['no_of_children']
            cid.emergency_contact_name = request.POST['emergency_contact_name']
            cid.relationship = request.POST['relationship']
            cid.emergency_contact_no = request.POST['emergency_contact_no']
            cid.family_member_name = request.POST['family_member_name']
            cid.family_member_relationship = request.POST['family_member_relationship']
            cid.family_member_phone_no = request.POST['family_member_phone_no']
            cid.family_member_birth_date = request.POST['family_member_birth_date']
            cid.institut_name = request.POST['institut_name']
            cid.subject = request.POST['subject']
            cid.institut_start_date = request.POST['institut_start_date']

            cid.institut_complate_date = request.POST['institut_complate_date']
            cid.institut_degree_name = request.POST['institut_degree_name']
            cid.institut_degree_grade = request.POST['institut_degree_grade']

            print("=========> Profile update")
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']

            cid.save()
             
            context = {
                "uid" : uid,
                "cid" : cid                            
            }
            return render(request,'myapp/profile.html',context)
        

def add_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        hid = Hr.objects.get(user_id = uid)
        print("Out")

        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['']
            contact_no = request.POST['contact_no']
            address = request.POST['address']
            email = request.POST['email']
            birth_date = request.POST['birth_date']
            special_interests = request.POST['special_interests']
            education = request.POST['education']
            pic = request.POST['pic']
            department = request.POST['department']
            gender = request.POST['gender']
            age = request.POST['age']
            date_of_join = request.POST['date_of_join']
            nationality = request.POST['nationality']
            religion = request.POST['religion']
            marital_status = request.POST['marital_status']
            no_of_children = request.POST['no_of_children']
            emergency_contact_name = request.POST['emergency_contact_name']
            relationship = request.POST['relationship']
            emergency_contact_no = request.POST['emergency_contact_no']
            bank_name = request.POST['bank_name']
            bank_account_no = request.POST['bank_account_no']
            state = request.POST['state']
            country = request.POST['country']
            pin_code = request.FILES['pin_code']
            family_member_name = request.POST['family_member_name']
            family_member_relationship = request.POST['family_member_relationship']
            family_member_birth_date = request.POST['family_member_birth_date']
            family_member_phone_no = request.POST['family_member_phone_no']
            institut_name = request.POST['institut_name']
            subject = request.POST['subject']
            institut_start_date = request.POST['institut_start_date']
            institut_complate_date = request.POST['institut_complate_date']
            institut_degree_name = request.POST['institut_degree_name']
            institut_degree_grade = request.POST['institut_degree_grade']
            
            password_list = ['ac7889','avi92884','aa456','ddy65','asdf54']
            password = email[3:7]+contact_no[5:8]+choice(password_list)

            uid = User.objects.create(email = email, password = password, role = 'Employees')
            eid = Employees.objects.create(user_id = uid,first_name = first_name, last_name = last_name, contact_no = contact_no, address = address, email = email, birth_date = birth_date, 
                                           special_interests = special_interests, education = education, pic = pic, department = department, gender = gender, age = age, date_of_join = date_of_join,
                                            nationality = nationality, religion = religion, marital_status = marital_status, no_of_children = no_of_children, emergency_contact_name = emergency_contact_name,
                                            relationship = relationship, emergency_contact_no = emergency_contact_no, bank_name = bank_name,
                                            bank_account_no = bank_account_no, state = state, country = country, pin_code = pin_code, family_member_name = family_member_name, family_member_relationship = family_member_relationship,
                                            family_member_birth_date = family_member_birth_date, family_member_phone_no = family_member_phone_no,institut_name = institut_name,subject = subject, institut_start_date = institut_start_date, institut_complate_date = institut_complate_date,
                                            institut_degree_name = institut_degree_name, institut_degree_grade = institut_degree_grade)


            if eid:
                print("In  111111111")
                send_mail("Hello ","Your Password is "+str(password),"avchauhan3920@gmail.com",[email])
                
                msg = "Employees Add Successfully !!!!!"
                context = {
                    'msg' : msg,
                    'uid' : uid,
                    'hid' : hid,
                }
                return render(request,'myapp/add-member.html',context)
            
        else:
            context = {
                'uid' : uid,
                'hid' : hid,
            }
            return render(request,'myapp/add-member.html',context)
        
    else:
        return redirect('login')