from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def cadastro_user(request):
    if request.method == "GET": # se method http for GET 
        if request.user.is_authenticated: # se user estiver logado vai para raiz 
            return redirect('/home')
        return render(request, 'cadastro.html') # se user não estiver logado vai para cadastro 
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

    if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
        return redirect('/cadastro')     
         
    usuario = User.objects.filter(username=username)
    
    if usuario.exists():
        return redirect('/cadastro')
    try:
        usuario = User.objects.create_user(username=username,
        email=email,
        password=senha)
        usuario.save()
        return redirect('/logar')
    except:
        return redirect('/cadastro')         
        
def logar_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'logar.html')
    elif request.method == "POST":
        # username = request.POST['username']
        # password = request.POST['password']
        # pode ser tbm
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=password)
        if not usuario:
            return redirect('/logar')
        else:
            auth.login(request, usuario)
            return render(request,'home.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/logar')
