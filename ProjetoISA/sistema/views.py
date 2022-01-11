from django.shortcuts import render
from django.http.response import HttpResponse

from sistema.forms import QuestionarioForm


def guia(request):
    return render(request, 'sistema/guia.html')


def questionario(request):
    context = {}
    form = QuestionarioForm()
    context['form'] = form
    return render(request, 'sistema/questionario.html', context)


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