from django.contrib import admin
from comunicados.models import *


# Register your models here.
@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'emisor',
        'asignatura'
    )


admin.site.register(DocumentoComunicado)
