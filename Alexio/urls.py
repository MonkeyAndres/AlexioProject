
from django.conf.urls import url, include
from django.contrib import admin
from setup import urls as setupUrls
from login import urls as loginUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^setup/', include(setupUrls)),
    url(r'^login/', include(loginUrls)),
]
