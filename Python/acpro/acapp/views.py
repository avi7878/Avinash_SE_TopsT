from django.shortcuts import render,redirect
from .models import user
from django.http import HttpResponse
# Create your views here.

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        salary = request.POST['salary']
        photo = request.FILES['photo']

        User = user(name=name,email=email,password=password,city=city,salary=salary,photo=photo)

        User.save()
        return render(request,"add.html") 
    return render(request,"add.html")

def view(request):
    User = user.objects.all()
    return render(request,"view.html",{'User':User})

def delete(request,id):
    User = user.objects.get(id=id)
    User.delete()
    return redirect("/view")

def edit(request,id):
    User = user.objects.get(id=id)
    data = user.objects.all()

    if request.method == "POST":
        User.name = request.POST['name']
        User.email = request.POST['email']
        User.password = request.POST['password']
        User.city = request.POST['city']
        User.salary = request.POST['salary']

        if 'photo' in request.FILES:
            User.photo = request.FILES['photo']

        # User.name=name
        # User.email=email
        # User.password=password
        # User.city=city
        # User.salary=salary
        # User.photo=photo
        User.save()

        return redirect('/view')
    return render(request,'edit.html',{'User':User,'data':data})

def search(request):
    if request.method == 'POST':
        User_id = request.POST.get('User_id')
        if User_id:
            User = user.objects.get(id=User_id)
            return render(request, 'user_detail.html', {'User': User})
    
    return render(request, 'search.html')