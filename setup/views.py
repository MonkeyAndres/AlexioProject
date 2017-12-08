# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
import uuid

setupTemplate = 'setup.html'


def setupIndex(request):
    return render(request, setupTemplate)


def crearAsignaturasView(request):  # VISTA
    if request.method == 'POST':
        datosFormulario = request.POST
        formAsignatura = AsignaturaForm(datosFormulario)

        if formAsignatura.is_valid():
            guardarAsignatura(formAsignatura)
            return HttpResponseRedirect('/setup/crearAsignaturas')

    context = crearContextoAsignaturas()
    return render(request, setupTemplate, context)


def guardarAsignatura(formAsignatura):
    nuevaAsignatura = formAsignatura.save()
    nuevaAsignatura.save()


def crearContextoAsignaturas():
    formAsignatura = AsignaturaForm()
    todasAsignaturas = Asignatura.objects.all().order_by('id')
    context = {
        'form': formAsignatura,
        'todasAsignaturas': todasAsignaturas,
        'tipoFormulario': 'Asignaturas'
    }
    return context


def crearProfesoresView(request):   # VISTA
    if request.method == 'POST':
        datosFormulario = request.POST
        formUsuario = ProfesorForm(datosFormulario)

        if formUsuario.is_valid():
            guardarUsuario(formUsuario)
            return HttpResponseRedirect('/setup/crearProfesores')

    context = crearContextoProfesor()
    return render(request, setupTemplate, context)


def crearAlumnosView(request):  # VISTA
    if request.method == 'POST':
        datosFormulario = request.POST
        formUsuario = AlumnoForm(datosFormulario)

        if formUsuario.is_valid():
            guardarUsuario(formUsuario)
            return HttpResponseRedirect('/setup/crearAlumnos')

    context = crearContextoAlumno()
    return render(request, setupTemplate, context)


def guardarUsuario(formUsuario):
    nuevoUsuario = formUsuario.save()
    datosUsuario = generarDatosUsuario(nuevoUsuario)
    usuarioCompleto = completarUsuario(nuevoUsuario, datosUsuario)
    usuarioCompleto.save()


def generarDatosUsuario(datosFormulario):
    generatedUsername = generarUser(datosFormulario)
    generatedPassword = generarPass(datosFormulario)
    generetedToken = generarToken()

    datos = {
        'username': generatedUsername,
        'password': generatedPassword,
        'token': generetedToken
    }

    return datos


def completarUsuario(nuevoUsuario, datosUsuario):
    nuevoUsuario.username = datosUsuario.get('username')
    nuevoUsuario.password = datosUsuario.get('password')
    nuevoUsuario.token = datosUsuario.get('token')

    return nuevoUsuario


def crearContextoProfesor():
    formProfesor = ProfesorForm()
    todosProfesores = Profesor.objects.all().order_by('id')
    context = {
        'form': formProfesor,
        'todosProfesores': todosProfesores,
        'tipoFormulario': 'Profesores'
    }
    return context


def crearContextoAlumno():
    formAlumno = AlumnoForm()
    todosAlumnos = Alumno.objects.all().order_by('id')
    context = {
        'form': formAlumno,
        'todosAlumnos': todosAlumnos,
        'tipoFormulario': 'Alumnos'
    }
    return context


def crearClasesView(request):   # VISTA
    if request.method == 'POST':
        datosFormulario = request.POST

        formRelleno = CursoForm(datosFormulario)

        if formRelleno.is_valid():
            nuevaClase = formRelleno.save()
            nuevaClase.save()

            return HttpResponseRedirect('/setup/crearClases')

    formClase = CursoForm()
    todasClases = Curso.objects.all().order_by('id')
    context = {
        'form': formClase,
        'todasClases': todasClases,
        'tipoFormulario': 'Cursos'
    }

    return render(request, setupTemplate, context)


def generarUser(datosFormulario):
    nombre = datosFormulario.nombre
    apellido = datosFormulario.apellido
    username = apellido + "." + nombre

    userDisponible = verificarDisponibilidadUser(username)

    if not userDisponible:
        username = generarUserDisponible(username)

    return username


def verificarDisponibilidadUser(username):
    allProfesores = Profesor.objects.filter(username=username)
    allAlumnos = Alumno.objects.filter(username=username)

    if allAlumnos or allProfesores:
        return False
    else:
        return True


def generarUserDisponible(username):
    itinerator = 1
    tryUser = username

    while not verificarDisponibilidadUser(tryUser):
        tryUser = username + "." + str(itinerator)
        itinerator = itinerator + 1
    return tryUser


def generarPass(datosFormulario):
    nombre = datosFormulario.nombre
    apellido = datosFormulario.apellido

    return "soy" + apellido.capitalize() + nombre.capitalize()


def generarToken():
    token = str(uuid.uuid4())
    return token
