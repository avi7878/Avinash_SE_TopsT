from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")


def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"myapp/index.html",context)
        else:
            pass

    elif request.POST:
        print("Submit buttom hit")
        p_email = request.POST['email']
        p_password = request.POST['password']
        print("Email ==== >>> ",p_email)
        try:
            uid = User.objects.get( email = p_email)
            print("Object uid = ",uid)

            if uid.password == p_password:
                if uid.role=='Chairman':
                    cid = Chairman.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    print(cid)
                    context = {
                        'uid' : uid,
                        'cid' : cid,
                    }
                    return render(request,"myapp/index.html",context)

                else:
                    pass
            else:
                print("Invalid password")
                context = {
                    "e_msg" : "Invalid password"
                }
            return render(request,"myapp/login.html",context)
        except:
            context = {
                    "e_msg" : "Invalid Email or Password"
                }
            return render(request,"myapp/login.html",context)
    else:
        print("only page refresh")
    return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")
    
def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"myapp/profile.html",context)
    
    
def change_password(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            current_passowrd = request.POST['currentpassword']
            new_passowrd = request.POST['newpassword']
            if uid.password == current_passowrd:
                uid.password = new_passowrd
                uid.save()  
                
                print("password ==> ",uid.password )
                context = {
                            "uid" : uid,
                            "cid" : cid,
                }
                return render(request,"myapp/profile.html",context)
        
            else:
                e_msg = "Invalid current password"
                del request.session['email']
                context = {
                    'e_msg' : e_msg,
                }
                return render(request,"myapp/login.html",context)
        context = {
                        "uid" : uid,
                        "cid" : cid,
        }
        return render(request,"myapp/profile.html",context)

def update_chairman_profile(request):
        if 'email' in request.session:
            uid = User.objects.get(email = request.session['email'])
            if uid.role == 'Chairman':
                cid = Chairman.objects.get(user_id = uid)   

                cid.first_name = request.POST['first_name']
                cid.last_name = request.POST['last_name']
                cid.contact_no = request.POST['contact_no']
                
                if "pic" in request.FILES:
                    cid.pic = request.FILES['pic']

                cid.save()

                context = {
                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request,"myapp/profile.html",context)
            
def add_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                nid = Notice.objects.create(notice_title = request.POST['notice_title'],notice_description = request.POST['notice_description'])

                if "pic" in request.FILES and "video" in request.FILES:
                    nid = Notice.objects.create(notice_title = request.POST['notice_title'],notice_description = request.POST['notice_description'],pic = request.FILES['pic'],video = request.FILES['video'])
                    
                elif "pic" in request.FILES:
                    nid = Notice.objects.create(notice_title = request.POST['notice_title'],notice_description = request.POST['notice_description'],pic = request.FILES['pic'])

                elif "video" in request.FILES:
                    nid = Notice.objects.create(notice_title = request.POST['notice_title'],notice_description = request.POST['notice_description'],video = request.FILES['video'])

                context = {
                    "uid" : uid,
                    "cid" : cid,
                }
                return render(request,"myapp/add-notice.html",context)

            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-notice.html",context)
        else:

            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-notice.html",context)

def view_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            nall = Notice.objects.all()
            context = {
                "uid" : uid,
                "cid" : cid,
                "nall" : nall,
            }
            return render(request,"myapp/list.html",context)

def edit_notice(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            nid = Notice.objects.get(id = pk)
            context = {
                "uid" : uid,
                "cid" : cid,
                "nid" : nid,
            }
            return render(request,"myapp/edit_notice.html",context)