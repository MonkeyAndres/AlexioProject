
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', setupIndex),
    url(r'^crearAsignaturas/$', crearAsignaturasView),
    url(r'^crearProfesores/$', crearProfesoresView),
    url(r'^crearAlumnos/$', crearAlumnosView),
    url(r'^crearClases/$', crearClasesView),
]
