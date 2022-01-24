from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.http import JsonResponse
from django.core import serializers

from sistema.forms import (
    QuestionarioForm, 
    PessoaForm,
    LocalizacaoForm
)
from sistema.models import Localizacao, Pessoa


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


def check_pessoas(request):
    if request.method == "GET":
        serialized_pessoas = serializers.serialize('json', Pessoa.objects.all())
        return JsonResponse({"pessoas": serialized_pessoas}, status=200)
    return JsonResponse({"error": ""}, status=400)


def pessoa_nova(request):
    context = {}
    close = 'false'
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        close = 'true'
        #return HttpResponse('<script type="text/javascript">window.close()</script>')
    context['form'] = form
    context['close'] = close

    return render(request, 'sistema/aux_form.html', context)


def check_localizacoes(request):
    if request.method == "GET":
        serialized_localizacoes = serializers.serialize('json', Localizacao.objects.all())
        return JsonResponse({"localizacoes": serialized_localizacoes}, status=200)
    return JsonResponse({"error": ""}, status=400)


def localizacao_nova(request):
    context = {}
    form = LocalizacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    context['form'] = form

    return render(request, 'sistema/aux_form.html', context)


def indicadores(request):
    context = {}
    pessoas = Pessoa.objects.all()
    context['options'] = pessoas

    return render(request, 'sistema/indicadores.html', context)


def relatorio(request):
    return render(request, 'sistema/relatorio.html')


def plano_adequacao(request):
    return render(request, 'sistema/plano_adequacao.html')


def formulas(request):
    return render(request, 'sistema/formulas.html')


def banco_de_dados(request):
    return render(request, 'sistema/banco_de_dados.html')