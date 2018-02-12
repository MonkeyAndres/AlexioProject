from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from comunicados.views import obtenerToken, obtenerAlumnoByToken
from .models import Trabajo, EntregaTrabajoOnline


def TrabajosView(request):
    token = obtenerToken(request)
    alumno = obtenerAlumnoByToken(token)
    trabajos = obtenerTrabajos(alumno)
    contexto = crearContexto(trabajos)
    # return render(request, "dashboard.html", contexto)
    return HttpResponse(trabajos)


def obtenerTrabajos(alumno):
    trabajosActuales = obtenerTrabajosActuales()
    trabajosAlumno = filtrarTrabajosAlumno(trabajosActuales, alumno)
    trabajosNoEntregados = filtrarTrabajosSinEntrega(trabajosAlumno, alumno)
    return trabajosNoEntregados


def obtenerTrabajosActuales():
    trabajosActuales = Trabajo.objects.filter(fechaEntrega__gte=timezone.now())
    return trabajosActuales


def filtrarTrabajosAlumno(trabajosActuales, alumno):
    trabajosAlumno = []
    for trabajo in trabajosActuales:
        if trabajo.asignatura.curso == alumno.curso:
            trabajosAlumno.append(trabajo)
    return trabajosAlumno


def filtrarTrabajosSinEntrega(trabajosAlumno, alumno):
    for trabajo in trabajosAlumno:
        if trabajo.online is True:
            if existEntrega(trabajo, alumno):
                trabajosAlumno.remove(trabajo)
    return trabajosAlumno


def existEntrega(trabajo, alumno):
    try:
        EntregaTrabajoOnline.objects.get(
            trabajo=trabajo,
            alumno=alumno
        )
        return True
    except Exception:
        return False


def crearContexto(trabajos):
    pass
