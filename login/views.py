# Create your views here.
from django.shortcuts import render, redirect
from setup.models import Profesor, Alumno


contextIncorrectUser = {'errorMessage': "Ha introducido mal el usuario"}
contextIncorrectPasswd = {'errorMessage': "Ha introducido mal la contraseña"}


def loginMain(request):
    if request.method == "POST":
        userData = extractRequestData(request)
        userObject = getUser(userData.get('username'))
        response = makeLogin(userObject, userData.get('password'), request)
        return response
    else:
        if 'token' in request.session:
            token = request.session["token"]
            response = comprobarToken(token, request)
            return response
        else:
            return render(request, "login.html")


def comprobarToken(token, req):
    if isTokenAlumno(token) or isTokenProfesor(token):
        response = redirect("/")
    else:
        borrarCokieToken(req)
        response = redirect("/login")
    return response


def borrarCokieToken(req):
    del req.session["token"]
    return True


def isTokenAlumno(token):
    try:
        Alumno.objects.get(token=token)
        return True
    except Exception:
        return False


def isTokenProfesor(token):
    try:
        Profesor.objects.get(token=token)
        return True
    except Exception:
        return False


def makeLogin(userObject, password, request):
    if not userObject:
        return render(request, "login.html", contextIncorrectUser)
    else:
        return logIn(userObject, password, request)


def getUser(username):
    if isProfesor(username):
        user = obtenerProfesor(username)
    elif isAlumno(username):
        user = obtenerAlumno(username)
    else:
        user = False
    return user


def extractRequestData(request):
    username = request.POST['user']
    password = request.POST['password']
    data = {
        'username': username,
        'password': password,
    }
    return data


def isProfesor(user):
    try:
        Profesor.objects.get(username=user)
        return True
    except Exception:
        return False


def isAlumno(user):
    try:
        Alumno.objects.get(username=user)
        return True
    except Exception:
        return False


def obtenerProfesor(user):
    userObject = Profesor.objects.get(username=user)
    return userObject


def obtenerAlumno(user):
    userObject = Alumno.objects.get(username=user)
    return userObject


def comprobarDatos(userObject, password):
    if userObject.password == password:
        return True
    else:
        return False


def setTokenCookie(userObject, request):
    if 'token' not in request.session:
        request.session["token"] = userObject.token
        response = redirect('/')
        return response
    else:
        return redirect('/')


def logIn(userObject, password, request):
    datosCorrectos = comprobarDatos(userObject, password)
    if datosCorrectos:
        response = setTokenCookie(userObject, request)
        return response
    else:
        return render(request, "login.html", contextIncorrectPasswd)
