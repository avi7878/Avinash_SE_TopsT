from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'myapp/admin-dashboard.html')
    
def login(request):
    return render(request,'myapp/login.html')

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")