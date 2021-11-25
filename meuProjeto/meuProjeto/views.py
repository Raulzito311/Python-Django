from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nome = "Raulindao"
    return render(request, 'index.html', {"nome" : nome})