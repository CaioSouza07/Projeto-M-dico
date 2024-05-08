from django.shortcuts import render , redirect , HttpResponse
from .models import Especialidades

# Create your views here.

def cadastro_medico(request):
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request , "cadastro_medico.html" , {'especialidades': especialidades})
    
    elif request.method == "POST":

        crm = request.POST.get("crm")
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade') 
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        return HttpResponse(f'{especialidade} e o {cim}')
    