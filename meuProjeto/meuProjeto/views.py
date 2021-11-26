from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'm'
    nome = 'Diogro'
    return render(request, 'index.html', {'sex' : sexo, 'name' : nome})