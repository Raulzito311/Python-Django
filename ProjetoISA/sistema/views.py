from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from sistema.forms import QuestionarioForm
from sistema.models import Questionario


def guia(request):
    return render(request, 'sistema/guia.html')


def questionario(request):
    #import pdb;pdb.set_trace() # uncomment this line so it creates a breakpoint here
    context = {}
    context['message'] = ''
    form = QuestionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = QuestionarioForm()
        context['message'] = 'Questionário salvo com sucesso!'
    context['form'] = form
    return render(request, 'sistema/questionario.html', context)


def questionario_novo(request):
    status = ''
    mensagem = ''
    if request.method == 'POST':
        try:
            questionario = {}
            questionario['croqui'] = request.POST.get('croqui')
            questionario['colaborador'] = request.POST.get('colaborador')
            questionario['beneficiario'] = request.POST.get('beneficiario')
            questionario['localizacao'] = request.POST.get('localizacao')

            Questionario.objects.create(**questionario)
        except Exception as e:
            status = 'show'
            mensagem = str(e)
        else:
            status = 'show'
            mensagem = 'Contato realizado com sucesso'

    return render(request, 'website/contato.html', {'status' : status, 'mensagem' : mensagem})


def indicadores(request):
    return render(request, 'sistema/indicadores.html')


def relatorio(request):
    return render(request, 'sistema/relatorio.html')


def plano_adequacao(request):
    return render(request, 'sistema/plano_adequacao.html')


def formulas(request):
    return render(request, 'sistema/formulas.html')


def banco_de_dados(request):
    return render(request, 'sistema/banco_de_dados.html')