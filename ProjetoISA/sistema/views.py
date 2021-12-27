from django.shortcuts import render
from django.http.response import HttpResponse

from sistema.forms import QuestionarioForm


def home(request):
    context = {}
    form = QuestionarioForm()
    context['mensagem'] = 'Olá meu caro'
    context['form'] = form
    return render(request, 'sistema/home.html', context)