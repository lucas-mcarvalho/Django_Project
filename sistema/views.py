from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login 

class Login(View):
    """
    Class based view para a tela de login
    """
    def get(self, request):
        contexto = {}
        return render(request, 'login.html', contexto)
    
    def post(self, request):
        usuario = request.POST.get('usuario') 
        senha = request.POST.get('senha')  

        user = authenticate(request, username=usuario, password=senha)
        
        if user is not None:
            if user.is_active:
                auth_login(request, user) 
                return redirect("veiculo/")
            else:
                return render(request, 'login.html', {'mensagem': 'Sua conta está desativada.'})
        
        else:
            return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos.'})