
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static

from gestao_rh import settings

urlpatterns = [
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('documento/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    #path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('accounts/', include('django.contrib.auth.urls')),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
