from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    return HttpResponse('CLIENTES: Maria, Jose, Joao')

def cliente_id(request, id):
    return HttpResponse('CLIENTES: detalhe do cliente ' + str(id))

def cliente_nome(request, nome):
    return HttpResponse('CLIENTES: detalhe do cliente ' + nome)