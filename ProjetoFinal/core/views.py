from django.shortcuts import render, redirect
from .models import (
    Mensalista,
    MovMensalista,
    MovRotativo, 
    Pessoa, 
    Veiculo
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm
)

def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


# LISTAR


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_movmensalistas(request):
    mov_mensal = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'mov_mensal': mov_mensal})


# CRIAR


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')