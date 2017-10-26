from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Asignatura)


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'asignaturaPrincipal',
        'asignaturaSecundaria'
    )


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'tutor'
    )


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'edad',
        'email',
        'clase'
    )
