from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.


def logar_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # pode ser tbm
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        user = auth.authenticate (request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request,'home.html')
        else:
            return redirect('/auth/logar')

def logout_view(request):
    logout(request)
    return redirect('/auth/logar')
        