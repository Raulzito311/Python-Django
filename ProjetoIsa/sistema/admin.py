from django.contrib import admin

from sistema.models import (
    TipoPosse,
    TipoOcupacao,
    TipoRecHidrico,

    Pessoa, 
    Imovel,
    Questionario,

    Ocupacao,
    RecHidrico,
    AreasNaoContiguas
)


admin.site.register(TipoPosse)
admin.site.register(TipoOcupacao)
admin.site.register(TipoRecHidrico)

admin.site.register(Pessoa)
admin.site.register(Imovel)
admin.site.register(Questionario)

admin.site.register(Ocupacao)
admin.site.register(RecHidrico)
admin.site.register(AreasNaoContiguas)