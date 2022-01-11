from django.urls import path
from .views import (
    guia,
    questionario,
    indicadores,
    relatorio,
    plano_adequacao,
    formulas,
    banco_de_dados
)

urlpatterns = [
    path('', guia, name='system_guia'),
    path('questionario/', questionario, name='system_questionario'),
    path('indicadores/', indicadores, name='system_indicadores'),
    path('relatorio/', relatorio, name='system_relatorio'),
    path('plano-adequacao/', plano_adequacao, name='system_plano_adequacao'),
    path('formulas/', formulas, name='system_formulas'),
    path('banco-de-dados/', banco_de_dados, name='system_banco_de_dados'),
]