from django.shortcuts import render, redirect
from .models import (
    Mensalista,
    MovMensalista,
    MovRotativo, 
    Pessoa, 
    Veiculo
)

from .forms import PessoaForm

def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_movmensalistas(request):
    mov_mensal = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'mov_mensal': mov_mensal})
