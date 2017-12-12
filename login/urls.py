
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', loginMain),
    url(r'^exit/$', logOut)
]
