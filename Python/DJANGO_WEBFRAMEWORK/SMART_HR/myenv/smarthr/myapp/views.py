from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'myapp/login.html')
    
def login(request):
    if request.POST:
        print("Submit buttom hit")
    else:
        print("Only page refresh")
    return render(request,'myapp/login.html')

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")