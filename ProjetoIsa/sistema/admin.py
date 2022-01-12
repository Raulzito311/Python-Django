from django.contrib import admin

from sistema.models import (
    Localizacao,
    Pessoa, 
    Questionario
)


admin.site.register(Pessoa)
admin.site.register(Localizacao)
admin.site.register(Questionario)
