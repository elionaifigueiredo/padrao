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
        senha = request.POST.get('senha')
        #nao pode ter um espaço vazio na esquerda e nem na direita
         
    usuario = User.objects.filter(username=username)
    
    if usuario.exists():
        return redirect('/auth/cadastro')
    try:
        usuario = User.objects.create_user(username=username,
        email=email,
        password=senha)
        usuario.save()
        return redirect('/auth/logar')
    except:
        return redirect('/auth/cadastro')         
        
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
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return render(request,'home.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/auth/logar')
