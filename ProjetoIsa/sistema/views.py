from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from sistema.forms import (
    QuestionarioForm, 
    PessoaForm,
    LocalizacaoForm
)


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


def pessoa_nova(request):
    context = {}
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    context['form'] = form

    return render(request, 'sistema/aux_form.html', context)


def localizacao_nova(request):
    context = {}
    form = LocalizacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    context['form'] = form

    return render(request, 'sistema/aux_form.html', context)


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