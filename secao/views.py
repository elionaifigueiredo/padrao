from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')


@login_required(login_url='/logar')
def board(request):
    return HttpResponse('PAINEL DA PAGINA')