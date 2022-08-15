from django.conf.urls import url
from django.urls import path
from .views import home

urlpatterns = [
    #path('', include('apps.funcionarios.urls'),)
    path('', home, name='home'),
    #url(r'^$', home, name='index'),
]
