from django.shortcuts import render
from django.http import HttpResponse
from .models import *


 
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


