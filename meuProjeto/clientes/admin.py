from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

admin.site.register(Empregado)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
