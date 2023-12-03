from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#pagina inicial
def home(request):
    return render(request,'home.html')

#Cadastro de user
def create(request):
    return render(request,'create.html')

#inicio dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')

#logout de usuario
def logouts(request):
    logout(request)
    return redirect ('/plogin/')

#mudar de senha
def changePassword(request):
        user = User.objects.get(email=request.user.email)
        print(user)
        user.set_password('123456')
        user.save()
        logout(request)
        return redirect('/plogin/')

#Login de user
def plogin(request):
    return render(request,'plogin.html')


#Enviar dados de login para DB
def dologin(request):
    data = {}
    user = authenticate(username = request.POST['user'], password = request.POST['password'])
    
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou senha incorretos'
        data['class'] = 'alert-danger'
        return render(request,'plogin.html',data)
    

#Colocar dados no DB
def store(request):
    data = {}
    
#checar se senhas são iguais
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes '
        data['class'] = 'alert-danger'
#salvar usuario no banco de dados
    else:
        user = User.objects.create_user (request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        
        data['msg'] = 'Usuario cadastrado '
        data['class'] = 'alert-success'
        
    return render(request,'create.html', data)