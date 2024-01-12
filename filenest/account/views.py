from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")

# def fileview(request,id):
#     files_objs=File.objects.get(id=id)
#     context={"File_objs": files_objs}
#     return render(request, 'fileview.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            return render(request, "login.html", {'error_message': "Username dosen't exist"})
        user_obj=authenticate(username=username,password=password)
        if user_obj:
            auth_login(request, user_obj)
            print("Login successful")
            return redirect("/fileview")
        print("Login failed")
        return redirect("/login")
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {'error_message': 'Username already exists'})

        user_obj = User.objects.create_user(username=username, password=password, first_name=first_name)

        print("User registration successful")
        return redirect("/login")  

    return render(request, "register.html")
@login_required(login_url='/login')
def logout(request):
    # logout(request)
    return redirect("/login")
@login_required(login_url='/login')
def fileview(request):
    context={}
    try:
        files = File.objects.filter(User=request.user)
        context['files']=files
    except Exception as e:
        print(e)
    return render(request, "fileview.html", context)
    