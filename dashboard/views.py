from django.shortcuts import render, redirect
from login.views import isTokenAlumno, isTokenProfesor
from comunicados.views import obtenerToken, obtenerAlumnoByToken
from comunicados.views import obtenerComunicadosDashboard
from deberes.views import obtenerTrabajosDashboard


def MainView(request):
    if request.method == "GET":
        response = MainViewGet(request)
    return response


def MainViewGet(request):
    token = obtenerToken(request)

    if isTokenAlumno(token):
        response = dashboardAlumno(token, request)
    elif isTokenProfesor(token):
        response = dashboardProfesor(token)
    else:
        response = redirect("/login")
    return response


def dashboardAlumno(token, req):
    alumno = obtenerAlumnoByToken(token)
    comunicados = obtenerComunicadosDashboard(alumno)
    deberes = obtenerTrabajosDashboard(alumno)
    # Add there deberes and eventos
    context = buildContext(alumno, comunicados, deberes)
    return render(req, "dashboard.html", context)


def buildContext(alumno, comunicados, deberes):
    context = {
        "templateStyle": "dashboard",
        "alumno": alumno,
        "comunicados": comunicados,
        "deberes": deberes
    }
    return context
