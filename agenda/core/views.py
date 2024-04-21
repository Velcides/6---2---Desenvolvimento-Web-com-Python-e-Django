from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User

# Create your views here.

# Def de redirecionamento para o endereço padrão.
#def index(request):
#    return redirect('/agenda/')

# Renderizando a tela de login.
def login_user(request):
    return render(request, 'login.html') 

# Criando a função de login.
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return redirect('/')

# Criando a função de logout.
def logout_user(request):
    logout(request)
    return redirect('/')

# Exibindo o HTML da agenda, de listagem de eventos.
@login_required(login_url='/login/') # Exigindo o login.
def lista_eventos(request):
    # Definindo filtro para pegar eventos apenas do usuário logado.
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual) # __gt greater than, para pegar apenas eventos de datas a frente.
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/') # Exigindo o login.
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados) # Renderizando o html de inserção de eventos.

# View para salvar os dados.
@login_required(login_url='/login/') # Exigindo o login.
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        # Caso tenha esse id altera se não insere novo evento.
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            #Evento.objects.filter(id=id_evento).update(titulo=titulo, data_evento=data_evento, descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)

    return redirect('/')

# View para excluir dados.
@login_required(login_url='/login/') # Exigindo o login.
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
       raise Http404
     
    # Só deleta eventos referentes ao usuário que esta logado.
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404
    return redirect('/')

@login_required(login_url='/login/') # Exigindo o login.
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)