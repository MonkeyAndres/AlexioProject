from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from comunicados.views import obtenerToken, obtenerAlumnoByToken
from .models import Trabajo, EntregaTrabajoOnline


def TrabajosView(request):
    token = obtenerToken(request)
    alumno = obtenerAlumnoByToken(token)
    trabajos = obtenerTrabajos(alumno, "all")
    contexto = crearContexto(trabajos, alumno)
    return render(request, "dashboard.html", contexto)


def obtenerTrabajos(alumno, modelo):
    trabajosActuales = obtenerTrabajosActuales(alumno)

    if modelo == "dashboard":
        trabajosNoEntregados = filtrarTrabajosSinEntrega(trabajosActuales, alumno)
        return trabajosNoEntregados
    else:
        return trabajosActuales


def obtenerTrabajosActuales(alumno):
    trabajosActuales = Trabajo.objects.filter(fechaEntrega__gte=timezone.now())
    trabajosFiltrados = filtrarTrabajosAlumno(trabajosActuales, alumno)
    return trabajosFiltrados


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


def crearContexto(trabajos, alumno):
    context = {
        "allDeberes": trabajos,
        "templateStyle": "deberes",
        "alumno": alumno
    }
    return context


def obtenerTrabajosDashboard(alumno):
    trabajos = obtenerTrabajos(alumno, "dashboard")
    return trabajos
