from django.contrib import admin

from .models import *


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
    )


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'tutor'
    )


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = (
        'concepto',
        'profesor',
        'curso'
    )


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'edad',
        'email',
        'curso'
    )
