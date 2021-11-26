from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'm'
    nome = 'Diogro'
    lista = [
        {'nome': 'Pedro', 'sexo' : 'm'},
        {'nome': 'Maria', 'sexo' : 'f'},
        {'nome': 'Joaquina', 'sexo' : 'u'},
        {'nome': 'Joao', 'sexo' : 'm'},
    ]
    data = {'sexo' : sexo, 'nome' : nome, 'lista' : lista}
    return render(request, 'index.html', data)