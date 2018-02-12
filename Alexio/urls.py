
from django.conf.urls import url, include
from django.contrib import admin
from setup import urls as setupUrls
from login import urls as loginUrls
from comunicados import urls as comunicadosUrls
from deberes import urls as trabajosUrls
from dashboard.views import MainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^setup/', include(setupUrls)),
    url(r'^login/', include(loginUrls)),
    url(r'^comunicados/', include(comunicadosUrls)),
    url(r'^deberes/', include(trabajosUrls)),
    url(r'^$', MainView)
]
