from django.urls import path
from .views import (
    home, 

    lista_pessoas, 
    pessoa_novo,
    pessoa_update,
    pessoa_delete,

    lista_veiculos, 
    veiculo_novo,
    veiculo_update,
    veiculo_delete,

    lista_movrotativos,
    movrotativo_novo,
    movrotativo_update,
    movrotativo_delete,

    lista_mensalistas,
    mensalista_novo,
    mensalista_update,
    mensalista_delete,

    lista_movmensalistas,
    movmensalista_novo,
    movmensalista_update,
    movmensalista_delete
)

urlpatterns = [
    path('', home, name='core_home'),

    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),

    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', movrotativo_novo, name='core_movrotativo_novo'),
    path('mov-rot-update/<int:id>', movrotativo_update, name='core_movrotativo_update'),
    path('mov-rot-delete/<int:id>', movrotativo_delete, name='core_movrotativo_delete'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>', mensalista_delete, name='core_mensalista_delete'),

    path('mov-mensal/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path('mov-mensal-update/<int:id>', movmensalista_update, name='core_movmensalista_update'),
    path('mov-mensal-delete/<int:id>', movmensalista_delete, name='core_movmensalista_delete')
]
