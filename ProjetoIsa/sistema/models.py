from django.db import models
from django.utils.translation import gettext_lazy as _


class Pessoa(models.Model):
    nome = models.CharField(max_length=256)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome + ' - ' + self.cpf


class Localizacao(models.Model):
    coordenadas = models.CharField(max_length=50)
    municipio = models.CharField(max_length=256)
    estado = models.CharField(max_length=2)
    curso_agua = models.CharField(max_length=256)
    codigo = models.CharField(max_length=256)

    def __str__(self):
        return self.codigo + ' - ' + self.coordenadas


class Questionario(models.Model):
    
    croqui = models.CharField(max_length=256)
    data = models.DateField
    colaborador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='colaborador')
    beneficiario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='beneficiario')
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    #class Titulo(models.TextChoices):
    #    PROPRIETARIO = 'PR', _('Proprietário')
    #    POSSEIRO = 'PO', _('Posseiro')
    #    ASSENTADO = 'AS', _('Assentado')
    #    ARRENDATARIO = 'AR', _('Arrendatário')
    #    PARCEIRO = 'PA', _('Parceiro')
    #    USUFRUARIO = 'US', _('Usufruário')
    #    SUCESSAO = 'SU', _('Processo sucessório em andamento')
    #    PARTICIPACAO = 'PM', _('Participação da mulher na gestão')

    #titulo = models.CharField(max_length=2, choices=Titulo.choices, default=Titulo.PROPRIETARIO)
    #titulos = models.CharField(max_length=256)

    def __str__(self):
        return self.croqui
