from django.shortcuts import render , redirect , HttpResponse
from .models import Especialidades, DadosMedico, is_medico
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.

def cadastro_medico(request):

    dm = is_medico(request.user)
    print(dm)
    if dm == True:
        messages.add_message(request, constants.WARNING, 'Você já tem cadastro como médico!')
        return redirect('/medicos/abrir_horario')

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
        valorConsulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm = crm,
            nome = nome,
            cep = cep,
            rua = rua,
            bairo = bairro,
            numero = numero,
            cedulaIdentidadeMedica = cim,
            rg = rg,
            foto = foto,
            especialidade_id = especialidade,
            descricao = descricao,
            valorConsulta = valorConsulta,
            user = request.user
        )

        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso!')

        return redirect('/medicos/abrir_horario') 
    