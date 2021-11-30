from django.urls import path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    mensalista_novo
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mov-mensal/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('mov-rot-novo/', movrotativo_novo, name='core_movrotativo_novo'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo')
]
