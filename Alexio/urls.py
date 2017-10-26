
from django.conf.urls import url, include
from django.contrib import admin
from setup import urls as setupUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^setup/', include(setupUrls)),
]
