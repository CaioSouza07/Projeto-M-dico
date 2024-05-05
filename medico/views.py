from django.shortcuts import render , redirect , HttpResponse

# Create your views here.

def cadastro_medico(request):
    if request.method == "GET":
        return HttpResponse("oiiiiiiiiiiiiiiiii isaaaa da minha vidaaaaaaaaaaaaa")