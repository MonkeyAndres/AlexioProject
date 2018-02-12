from django.shortcuts import render, redirect
from django.http import HttpResponse

from login.views import isTokenAlumno, isTokenProfesor

from .models import *
from setup.models import Alumno, Profesor


def ComunicadosView(request):
    if request.method == "GET":
        response = ComunicadosGET(request)
    return response


def ComunicadosGET(request):
    token = obtenerToken(request)

    if isTokenAlumno(token):
        response = comunicadosGetAlumno(token, request)
    elif isTokenProfesor(token):
        response = comunicadosGetProfesor(token, request)
    else:
        response = redirect("/login")
    return response


def comunicadosGetAlumno(token, request):
    page = request.GET.get('page')
    alumno = obtenerAlumnoByToken(token)
    comunicados = obtenerComunicadosAlumno(alumno, page)
    context = buildAlumnoContext(alumno, comunicados)
    return render(request, "dashboard.html", context)


def obtenerAlumnoByToken(token):
    alumno = Alumno.objects.get(token=token)
    return alumno


def obtenerComunicadosAlumno(alumno, page):
    if not page:
        page = 1
    page = int(page)
    firtsItem = (page-1)*10
    lastItem = firtsItem+10
    comunicados = Comunicado.objects.filter(receptores=alumno.curso).order_by("-id")[firtsItem:lastItem]
    return comunicados


def buildAlumnoContext(alumno, comunicados):
    numeroPaginas = obtenerNumeroPaginas(comunicados)
    contextPaginas = range(1, numeroPaginas+1)
    context = {
        "templateStyle": "comunicados",
        "alumno": alumno,
        "allComunicados": comunicados,
        "numeroPaginas": contextPaginas
    }
    return context


def obtenerNumeroPaginas(comunicados):
    numeroComunicados = comunicados.count()
    numeroPaginas = numeroComunicados/10
    return int(numeroPaginas)


def comunicadosGetProfesor(token, request):
    page = request.GET.get('page')
    profesor = obtenerProfesorByToken(token)
    comunicados = obtenerComunicadosProfesor(profesor, page)
    return HttpResponse(comunicados)


def obtenerProfesorByToken(token):
    profesor = Profesor.objects.get(token=token)
    return profesor


def obtenerComunicadosProfesor(profesor, page):
    if not page:
        page = 0
    page = int(page)
    firtsItem = page*10
    lastItem = firtsItem+10
    comunicados = Comunicado.objects.filter(emisor=profesor).order_by("-id")[firtsItem:lastItem]
    return comunicados


def obtenerToken(request):
    try:
        token = request.session['token']
        return token
    except Exception:
        return False


def MostrarComunicadoView(request, comunicadoID):
    token = obtenerToken(request)
    comunicado = getComunicadoByID(comunicadoID, token)

    if tienePermiso(token, comunicado):
        marcarComunicadoLeido(comunicado, token)
        context = buildComunicadoContext(token, comunicado)
        return render(request, "dashboard.html", context)
    else:
        return redirect("/login")


def tienePermiso(token, comunicado):
    if isTokenAlumno(token):
        return comprobarPermisoAlumno(token, comunicado)
    elif isTokenProfesor(token):
        return comprobarPermisoProfesor(token, comunicado)
    else:
        return False


def comprobarPermisoAlumno(token, comunicado):
    alumno = obtenerAlumnoByToken(token)
    if alumno.curso in comunicado.receptores.all():
        return True


def comprobarPermisoProfesor(token, comunicado):
    profesor = obtenerProfesorByToken(token)
    if profesor.curso == comunicado.emisor:
        return True


def getComunicadoByID(comunicadoID, token):
    if token:
        comunicado = Comunicado.objects.get(pk=comunicadoID)
        return comunicado
    else:
        return False


def buildComunicadoContext(token, comunicado):
    alumno = obtenerAlumnoByToken(token)
    context = {
        "templateStyle": "comunicado",
        "alumno": alumno,
        "comunicado": comunicado,
        "documentos": obtenerDocumentos(comunicado)
    }
    return context


def obtenerDocumentos(comunicado):
    documentos = AdjuntoComunicado.objects.filter(comunicado=comunicado)
    return documentos


def marcarComunicadoLeido(comunicado, token):
    alumno = obtenerAlumnoByToken(token)
    if alumno not in comunicado.alumnosLeido.values():
        comunicado.alumnosLeido.add(alumno)
        comunicado.save()


def obtenerComunicadosDashboard(alumno):
    comunicados = Comunicado.objects.filter(receptores=alumno.curso).order_by("-id")[:5]
    comunicadosFiltrados = filtrarComunicadosDashboard(comunicados, alumno)
    return comunicadosFiltrados


def filtrarComunicadosDashboard(comunicados, alumno):
    comunicadosFiltrados = []
    for c in comunicados:
        if alumno not in c.alumnosLeido.all():
            comunicadosFiltrados.append(c)
    return comunicadosFiltrados
