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
    data['titulo'] = 'Pessoas'
    data['form'] = form
    data['create_url'] = 'core_pessoa_novo'
    data['update_url'] = 'core_pessoa_update'
    objs = []
    for obj in pessoas:
        atts = dict((name, getattr(obj, name)) for name in vars(obj) if not name.startswith('_'))
        objs.append(atts)
    data['objs'] = objs

    return render(request, 'core/listar.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['title'] = 'Pessoa'
    data['obj'] = pessoa
    data['form'] = form
    data['update_url'] = 'core_pessoa_update'
    data['delete_url'] = 'core_pessoa_delete'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update.html', data)


def pessoa_delete(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    data['obj'] = pessoa
    data['delete_url'] = 'core_pessoa_delete'

    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)


# VEÍCULOS


def lista_veiculos(request):
    data = {}
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data['titulo'] = 'Veículos'
    data['form'] = form
    data['create_url'] = 'core_veiculo_novo'
    data['update_url'] = 'core_veiculo_update'
    objs = []
    for obj in veiculos:
        atts = dict((name, getattr(obj, name)) for name in vars(obj) if not name.startswith('_'))
        objs.append(atts)
    data['objs'] = objs

    return render(request, 'core/listar.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['title'] = 'Veículo'
    data['obj'] = veiculo
    data['form'] = form
    data['update_url'] = 'core_veiculo_update'
    data['delete_url'] = 'core_veiculo_delete'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update.html', data)


def veiculo_delete(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    data['obj'] = veiculo
    data['delete_url'] = 'core_veiculo_delete'

    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MOVIMENTOS ROTATIVOS


def lista_movrotativos(request):
    data = {}
    movs = MovRotativo.objects.all()
    form = MovRotativoForm()
    data['titulo'] = 'Movimentos Rotativos'
    data['form'] = form
    data['create_url'] = 'core_movrotativo_novo'
    data['update_url'] = 'core_movrotativo_update'
    objs = []
    for obj in movs:
        atts = dict((name, getattr(obj, name)) for name in vars(obj) if not name.startswith('_'))
        objs.append(atts)
    data['objs'] = objs

    return render(request, 'core/listar.html', data)


def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def movrotativo_update(request, id):
    data = {}
    mov = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov)
    data['title'] = 'Movimento Rotativo'
    data['obj'] = mov
    data['form'] = form
    data['update_url'] = 'core_movrotativo_update'
    data['delete_url'] = 'core_movrotativo_delete'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update.html', data)


def movrotativo_delete(request, id):
    data = {}
    mov_rot = MovRotativo.objects.get(id=id)
    data['obj'] = mov_rot
    data['delete_url'] = 'core_movrotativo_delete'

    if request.method == 'POST':
        mov_rot.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MENSALISTAS


def lista_mensalistas(request):
    data = {}
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data['titulo'] = 'Mensalistas'
    data['form'] = form
    data['create_url'] = 'core_mensalista_novo'
    data['update_url'] = 'core_mensalista_update'
    objs = []
    for obj in mensalistas:
        atts = dict((name, getattr(obj, name)) for name in vars(obj) if not name.startswith('_'))
        objs.append(atts)
    data['objs'] = objs

    return render(request, 'core/listar.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['title'] = 'Mensalista'
    data['obj'] = mensalista
    data['form'] = form
    data['update_url'] = 'core_mensalista_update'
    data['delete_url'] = 'core_mensalista_delete'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update.html', data)


def mensalista_delete(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    data['obj'] = mensalista
    data['delete_url'] = 'core_mensalista_delete'

    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MOVIMENTOS MENSALISTAS


def lista_movmensalistas(request):
    data = {}
    movs = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data['titulo'] = 'Movimentos Mensalistas'
    data['form'] = form
    data['create_url'] = 'core_movmensalista_novo'
    data['update_url'] = 'core_movmensalista_update'
    objs = []
    for obj in movs:
        atts = dict((name, getattr(obj, name)) for name in vars(obj) if not name.startswith('_'))
        objs.append(atts)
    data['objs'] = objs

    return render(request, 'core/listar.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


def movmensalista_update(request, id):
    data = {}
    mov = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov)
    data['title'] = 'Movimento Mensalista'
    data['obj'] = mov
    data['form'] = form
    data['update_url'] = 'core_movmensalista_update'
    data['delete_url'] = 'core_movmensalista_delete'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update.html', data)


def movmensalista_delete(request, id):
    data = {}
    mov = MovMensalista.objects.get(id=id)
    data['obj'] = mov
    data['delete_url'] = 'core_movmensalista_delete'

    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)