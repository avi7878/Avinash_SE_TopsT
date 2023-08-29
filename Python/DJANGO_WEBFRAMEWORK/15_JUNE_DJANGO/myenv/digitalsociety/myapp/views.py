from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    if "email" in request.session:
        return render(request,"myapp/index.html")
    else:
        return render(request,"myapp/login.html")

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
            return render(request,"myapp/index.html",context)
        else:
            pass
    elif request.POST:
        print("Submit buttom hit")
        p_email = request.POST['email']
        p_password = request.POST['password']
        print("=====>>>> email = ",p_email)
        try:
            uid = User.objects.get(email = p_email)
            print("=====>>>> uid object  ",uid)
            if uid.password == p_password:
                if uid.role=="chairman":
                    cid = Chairman.objects.get(user_id = uid)
                    request.session['email']=uid.email
                    print(cid)
                    context = {
                        "uid" : uid,
                        "cid" : cid,
                    }
                    return render(request,"myapp/index.html",context)

                else:
                    pass
            else:
                print("====> invalid password")
                context = {
                    "e_msg" : "Invalid password"                
                }
            return render(request,"myapp/login.html",context)
            # get data from database - validation query
        except:
            context = {
                    "e_msg" : "Invalid Email or password"                
                }
            return render(request,"myapp/login.html",context)

    else:
        print("only page refresh")
    return render(request,"myapp/login.html")
    
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
            return render(request,"myapp/profile.html",context)
    return render(request,"myapp/profile.html",context)
        
def change_password(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'chairman':
            cid = Chairman.objects.get(user_id = uid)
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            if uid.password == current_password:
                uid.password = new_password
                uid.save #update
            else:
                e_msg = "Invalid Current Password"
                return render(request,"myapp/login.html")

            context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
            return render(request,"myapp/profile.html",context)