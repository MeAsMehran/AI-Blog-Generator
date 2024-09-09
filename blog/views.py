from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError

# Create your views here.


def welcome(request):
    return render(request, 'pages/welcome.html')


def mainPage(request):
    return render(request, 'pages/aiBlog.html')


def signupuser(request):
    form = UserCreationForm()
    
    if request.method == 'GET':
        return render(request, 'pages/signup.html', {'form': form , 'error': ''})
    else:
        if request.POST["fPassword"] == request.POST["sPassword"]:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['fPassword'])
                user.save()
                login(request, user)
                return redirect('aiBlogPage')
            except IntegrityError:
                return render(request, 'pages/signup.html', {'form': form, 'error': 'User is already Signed Up!'})
        else:
            return render(request, 'pages/signup.html', {'form': form, 'error': "password didn't match"})


def loginuser(request):
    form = AuthenticationForm()
    
    if request.method == "GET":
        return render(request, 'pages/login.html', {'form': form, 'error': ""})
    else:
        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'pages/login.html', {'form': form, 'error': "User not found!"})
        else:
            login(request, user)
            return redirect('aiBlogPage')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('welcomePage')


def allBlogs(request):

    if request.method == "GET":
        return render(request, 'pages/AllBlogs.html')


def blogDetail(request):
    pass




























