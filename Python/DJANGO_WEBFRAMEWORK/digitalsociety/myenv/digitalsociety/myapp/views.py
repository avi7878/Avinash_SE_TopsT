from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from random import *
from django.core.mail import send_mail
from django.contrib import messages
# from django.contrib.auth.models import User
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
            try:
                sid = SocietyMember.objects.get(user_id = uid)
                context = {
                            'uid' : uid,
                            'sid' : sid,
                        }
                return render(request,"myapp/index.html",context)
            except:
                return HttpResponse("Page not Found")
            
            # return render(request,"myapp/login.html")
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
            sid = SocietyMember.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'sid' : sid,
                        }
            return render(request,"myapp/index.html",context)
            # try:
            #     sid = SocietyMember.objects.get(user_id = uid)
            #     context = {
            #                 'uid' : uid,
            #                 'sid' : sid,
            #             }
            #     return render(request,"myapp/index.html",context)
            # except:
            #     return render(request,"myapp/login.html")

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
                    sid = SocietyMember.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    print(sid)
                    print("firstname ",sid.firstname)

                    context = {
                        'uid' : uid,
                        'sid' : sid,
                    }
                    return render(request,"myapp/index.html",context)
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
        else:
            sid = SocietyMember.objects.get(user_id = uid)    
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"myapp/member-profile.html",context)
    
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
            # else:
            #     sid = SocietyMember.objects.get(user_id = uid)

            #     sid.first_name = request.POST['first_name']
            #     sid.last_name = request.POST['last_name']
            #     sid.contact_no = request.POST['contact_no']         

            #     if 'pic' in request.FILES:
            #         sid.pic = request.FILES['pic'] 

            #     sid.save()    

            #     context = {
            #         'uid' : uid,
            #         'sid' : sid,
            #     }
            #     return render(request,"myapp/profiles.html",context)
            
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
            sid = SocietyMember.objects.get(user_id = uid)
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
                    "sid" : sid,
                }
                return render(request,"myapp/add-notice.html",context)

            context = {
                "uid" : uid,
                "sid" : sid,
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
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            nall = Notice.objects.all()
            context = {
                "uid" : uid,
                "sid" : sid,
                "nall" : nall,
            }
            return render(request,"myapp/list.html",context)

def edit_notice(request, pk):
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
        
def delete_notice(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            nid = Notice.objects.get(id = pk)

            nid.delete()
            nall = Notice.objects.all()
            context = {
                "uid" : uid,
                "cid" : cid,
                "nall" : nall,
            }
            return render(request,"myapp/list.html",context)

def forgot_password(request):
    print("hello")
    if request.POST:
        email = request.POST['email']
        otp = randint(1111,9999)
        print("================>>>",email)
        try:
            print("=====> inside  the try ")
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            
            send_mail("Forgot password","Your otp is "+str(otp),"avchauhan3920@gmail.com",[email])
            context = {
                    'email' : email
                }
            print("=======>>>>> change password ",email)
            print(otp)
            print(uid)
            return render(request,"myapp/change-password.html",context)
        except:
            context = {
                "e_msg" : "Invalid email address"     
                }   
            return render(request,"myapp/forgot_password.html",context)
    return render(request,"myapp/forgot_password.html")

def change_password_value(request):
    print("      Inside the save password   ")
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        print("--------------->>>email",email)
        uid = User.objects.get(email = email)
        print("--------------->>>email",email)
        if str(uid.otp) == otp:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                context = {
                    "email" : email,
                    "smsg" : "Password successfully changed"
                }
                return render(request,"myapp/login.html",context)
            else:
                emsg = "Invalid password"
                context = {
                    "email" : email,
                    "e_msg" : emsg
                }
                return render(request,"myapp/change-password.html",context)
        else:
            emsg = "Invalid Otp"
            context = {
                    "email" : email,
                    "e_msg" : emsg
            }
            return render(request,"myapp/change-password.html",context)
        
def register(request):
    # if "email" in request.session:
    #     uid = User.objects.get(email = request.session['email'])
    #     cid = Chairman.objects.get(user_id = uid)

    if request.method == 'POST':
        # user_id = uid,
        name = request.POST['name']
        email =  request.POST['email']
        contact_no =  request.POST['contact_no']
        password =  request.POST['password']
        gender =  request.POST['gender']
        subject =  request.POST.getlist('subject')
        city =  request.POST['city']
        if User.objects.filter(name=name).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create(name,email,contact_no,password,gender,subject,city)
            login(request, user)
            return redirect('index')
        return render(request,'myapp/register.html')
    return render(request,'myapp/register.html')
        # rall = Registration.objects.all()

    #     context = {
    #         # 'uid' : uid,
    #         # 'cid' : cid, 
    #         'rall' : rall,
    #     }
    #     return render(request,"myapp/register.html",context)
    # else:
    #     context = {
    #         # 'uid' : uid,
    #         # 'cid' : cid, 
    #     }
    #     return render(request,"myapp/register.html",context)
        
    # else:
    #     print("only page refreshhhhhhhhhhh")
    #     return redirect("login")
    # return render(request,"myapp/register.html")


def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            contact_no = request.POST['contact_no']
            city = request.POST['city']
            no_of_family_member = request.POST['no_of_family_member']
            house_no = request.POST['house_no']
            occupation = request.POST['occupation']
            job_address = request.POST['job_address']
            vahical_details = request.POST['vahical_details']
            date_of_birth = request.POST['date_of_birth']
            email = request.POST['email']
            blood_group = request.POST['blood_group']
            pic = request.FILES['pic']
            # if 'pic' in request.FILES:
            #     pic = request.FILES['pic']

            l1 = ['as789','asf2740','sfv521','khb354','zed354']
            password = email[4:7]+contact_no[3:7]+choice(l1)

            uid = User.objects.create(email = email,password = password,role = "Societymember")
            sid = SocietyMember.objects.create(user_id = uid,first_name = first_name,last_name = last_name,contact_no = contact_no,city = city,no_of_family_member = no_of_family_member,
                                               house_no = house_no,occupation = occupation, job_address = job_address, vahical_details = vahical_details,date_of_birth = date_of_birth,email = email,blood_group = blood_group,pic = pic)
            
            if sid:
                send_mail("Hello ","Your Password is "+str(password),"avchauhan3920@gmail.com",[email])
                
                msg = "successfully society member created !!"
                context = {
                'msg' : msg,
                'uid' : uid,
                'cid' : cid,
                }
                return render(request,"myapp/add-member.html",context)                
        else:
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"myapp/add-member.html",context)
    else:
        return redirect("login")

def all_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            sall = SocietyMember.objects.all()
            context = {
                    'uid' : uid,
                    'cid' : cid,
                    'sall' : sall, 
            }
            print("insideee the all member  page")
            return render(request,"myapp/all-member.html",context)
        else :
            sid = SocietyMember.objects.get(user_id = uid)
            sall = SocietyMember.objects.all()
            context = {
                    'uid' : uid,
                    'sid' : sid,
                    'sall' : sall, 
            }
            print("insideee the all member  page")
            return render(request,"myapp/all-member.html",context)           

def societyspecification_profile(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman" :
            cid = Chairman.objects.get(user_id = uid)
            sid = SocietyMember.objects.get(id = pk)

            context = {
                    'uid' : uid,
                    'cid' : cid, 
                    'sid' : sid,
                    
            }
            return render(request,"myapp/specific_profile.html",context)
        else :
            sid = SocietyMember.objects.get(user_id = uid)
            sid = SocietyMember.objects.get(id = pk)

            context = {
                    'uid' : uid,
                    'sid' : sid, 
                    'sid' : sid,
                    
            }
            return render(request,"myapp/specific_profile.html",context)

    
def member_profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                            'uid' : uid,
                            'cid' : cid,
                        }
            return render(request,"myapp/member-profile.html",context)

def update_member_profile(request):
        if 'email' in request.session:
            uid = User.objects.get(email = request.session['email'])
            if uid.role == 'societymember': 
                print("Inside the block !!!!!")
                sid = SocietyMember.objects.get(user_id = uid)   

                sid.first_name = request.POST['first_name']
                sid.last_name = request.POST['last_name']
                sid.contact_no = request.POST['contact_no']
            
                if "pic" in request.FILES:
                    sid.pic = request.FILES['pic']

                sid.save()

                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
                return render(request,"myapp/member-profile.html",context)
            print("Outside the block")
            return render(request,"myapp/member-profile.html")
            
def add_event(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                eid = event.objects.create(event_title = request.POST['event_title'],event_description = request.POST['event_description'])

                context = {
                    "uid" : uid,
                    "cid" : cid,
                }
                return render(request,"myapp/add-event.html",context)
            
            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-event.html",context)
        else:

            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-event.html",context)

def view_event(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            nall = event.objects.all()
            context = {
                "uid" : uid,
                "cid" : cid,
                "nall" : nall,
            }
            return render(request,"myapp/view-event.html",context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            nall = event.objects.all()
            context = {
                "uid" : uid,
                "sid" : sid,
                "nall" : nall,
            }
            return render(request,"myapp/view-event.html",context)
        

def add_complaints(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                cid = complaints.objects.create(complaints_description = request.POST['complaints_description'])

                context = {
                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request,"myapp/add-complaints.html",context)
            
            context = {
                    'uid' : uid,
                    'cid' : cid,
                }
            return render(request,"myapp/add-complaints.html",context)
            
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            if request.POST:
                cid = complaints.objects.create(complaints_description = request.POST['complaints_description'])

                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
                return render(request,"myapp/add-complaints.html",context)
            context = {
                    'uid' : uid,
                    'sid' : sid,
                }
            return render(request,"myapp/add-complaints.html",context)

def view_complaints(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            nall = complaints.objects.all()
            context = {
                'uid' : uid, 
                'cid' : cid,
                'nall' : nall,
            }
            return render(request,"myapp/view-complaints.html",context)
        else:
            sid = SocietyMember.objects.get(user_id = uid)
            nall = complaints.objects.all()

            context = {
                'uid' : uid,
                'sid' : sid,
                'nall' : nall,
            }
            return render(request,"myapp/view-complaints.html",context)
    
def add_maintainance(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            
            if request.POST:
                mid = maintainance.objects.create(title = request.POST['title'], amount = request.POST['amount'], duedate = request.POST['duedate'])
                
                context = {
                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request,"myapp/add-maintainance.html",context)
            context = {
                    'uid' : uid,
                    'cid' : cid,
                }
            return render(request,"myapp/add-maintainance.html",context)
        
        else:

            sid = SocietyMember.objects.get(user_id = uid)

            if request.POST:
                mid = maintainance.objects.create(title = request.POST['title'], amount = request.POST['amount'], duedate = request.POST['duedate'])

                context = {
                    'uid' : uid,
                    'sid' : sid,
                }
                return render(request,"myapp/add-maintainance.html",context)
            context = {
                    'uid' : uid,
                    'sid' : sid,
                }
            return render(request,"myapp/add-maintainance.html",context)

def all_maintainance(request):
    if 'email' in request.session:
          uid = User.objects.get(email = request.session['email'])
          if uid.role == 'Chairman':
              cid = Chairman.objects.get(user_id = uid)
              mall = maintainance.objects.all() 

              context = {
                  'uid' : uid,
                  'cid' : cid,
                  'mall' : mall,
              }
              return render(request,"myapp/all-maintainance.html",context)
          else:
              sid = SocietyMember.objects.get(user_id = uid)
              mall = maintainance.objects.all()

              context = {
                  'uid' : uid,
                  'sid' : sid,
                  'mall' : mall,
              }
              return render(request,"myapp/all-maintainance.html",context)
