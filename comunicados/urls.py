
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ComunicadosView),
    url(r'(?P<comunicadoID>\w{0,50})/$', MostrarComunicadoView)
]
