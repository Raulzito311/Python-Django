from django.shortcuts import render, redirect
from .models import (
    Mensalista,
    MovMensalista,
    MovRotativo, 
    Pessoa, 
    Veiculo
)

from .forms import (
    MensalistaForm,
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MovMensalistaForm
)

def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


# PESSOAS


def lista_pessoas(request):
    data = {}
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data['pessoas'] = pessoas
    data['form'] = form
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


# VEÍCULOS


def lista_veiculos(request):
    data = {}
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data['veiculos'] = veiculos
    data['form'] = form
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


# MOVIMENTOS ROTATIVOS


def lista_movrotativos(request):
    data = {}
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data['mov_rot'] = mov_rot
    data['form'] = form
    return render(request, 'core/lista_movrotativos.html', data)


def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def movrotativo_update(request, id):
    data = {}
    mov_rot = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rot)
    data['mov_rot'] = mov_rot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


# MENSALISTAS


def lista_mensalistas(request):
    data = {}
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data['mensalistas'] = mensalistas
    data['form'] = form
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


# MOVIMENTOS MENSALISTAS


def lista_movmensalistas(request):
    data = {}
    mov_mensal = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data['mov_mensal'] = mov_mensal
    data['form'] = form
    return render(request, 'core/lista_movmensalistas.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


def movmensalista_update(request, id):
    data = {}
    mov_mensal = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensal)
    data['mov_mensal'] = mov_mensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalista.html', data)