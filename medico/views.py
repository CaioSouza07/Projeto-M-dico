from django.shortcuts import render , redirect , HttpResponse

# Create your views here.

def cadastro_medico(request):
    if request.method == "GET":
        X = 1
        return render(request , "cadastro_medico.html" , {'teste': X})
    