from django.contrib import admin
from .models import *


@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    list_display = (
        'concepto',
        'asignatura',
        'online',
        'fechaEntrega'
    )


@admin.register(NotaTrabajo)
class NotaTrabajoAdmin(admin.ModelAdmin):
    list_display = (
        'trabajo',
        'notaNumerica',
        'alumno'
    )


@admin.register(EntregaTrabajoOnline)
class EntregaTrabajoOnlineAdmin(admin.ModelAdmin):
    list_display = (
        'trabajo',
        'alumno',
        'nota'
    )


@admin.register(AdjuntoTrabajo)
class AdjuntoTrabajoAdmin(admin.ModelAdmin):
    list_display = (
        'nombreArchivo',
        'trabajo'
    )


@admin.register(DocumentoEntrega)
class DocumentoEntregaAdmin(admin.ModelAdmin):
    list_display = (
        'nombreArchivo',
        'entrega'
    )
