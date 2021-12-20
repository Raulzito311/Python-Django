from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


@login_required()
def lista_pessoas(request):
    data = {}
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data['tag'] = 'Pes'
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


@login_required()
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required()
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['tag'] = 'Pes'
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


@login_required()
def pessoa_delete(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    data['tag'] = 'Pes'
    data['obj'] = pessoa
    data['delete_url'] = 'core_pessoa_delete'

    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)


# VEÍCULOS


@login_required()
def lista_veiculos(request):
    data = {}
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data['tag'] = 'Vei'
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


@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required()
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['tag'] = 'Vei'
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


@login_required()
def veiculo_delete(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    data['tag'] = 'Vei'
    data['obj'] = veiculo
    data['delete_url'] = 'core_veiculo_delete'

    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MOVIMENTOS ROTATIVOS


@login_required()
def lista_movrotativos(request):
    data = {}
    movs = MovRotativo.objects.all()
    form = MovRotativoForm()
    data['tag'] = 'MovRot'
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


@login_required()
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required()
def movrotativo_update(request, id):
    data = {}
    mov = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov)
    data['tag'] = 'MovRot'
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


@login_required()
def movrotativo_delete(request, id):
    data = {}
    mov_rot = MovRotativo.objects.get(id=id)
    data['tag'] = 'MovRot'
    data['obj'] = mov_rot
    data['delete_url'] = 'core_movrotativo_delete'

    if request.method == 'POST':
        mov_rot.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MENSALISTAS


@login_required()
def lista_mensalistas(request):
    data = {}
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data['tag'] = 'Mens'
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


@login_required()
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required()
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['tag'] = 'Mens'
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


@login_required()
def mensalista_delete(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    data['tag'] = 'Mens'
    data['obj'] = mensalista
    data['delete_url'] = 'core_mensalista_delete'

    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


# MOVIMENTOS MENSALISTAS


@login_required()
def lista_movmensalistas(request):
    data = {}
    movs = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data['tag'] = 'MovMens'
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


@login_required()
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required()
def movmensalista_update(request, id):
    data = {}
    mov = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov)
    data['tag'] = 'MovMens'
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


@login_required()
def movmensalista_delete(request, id):
    data = {}
    mov = MovMensalista.objects.get(id=id)
    data['tag'] = 'MovMens'
    data['obj'] = mov
    data['delete_url'] = 'core_movmensalista_delete'

    if request.method == 'POST':
        mov.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)