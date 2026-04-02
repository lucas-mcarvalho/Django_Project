from django.views.generic import View
from django.shortcuts import render

class Login(View):

    """
    Class based view para a tela de login
    """
    def get(self,request):

        contexto = {}
        return render(request,'login.html',contexto)