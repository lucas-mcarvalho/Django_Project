from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo! Bem-vindo ao meu site Django.")