from django.conf.urls import url
from django.urls import path
from .views import (
    DocumentoNovo,
)

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoNovo.as_view(), name='create_document'),
    #path('novo/<funcionario_id>/', DocumentoNovo.as_view(), name='create_document'),
    #path('novo/(?P<slug>[funcionario_id)/', DocumentoNovo.as_view(), name='create_document'),
    #path('delete/<int:pk>/', DocumentoDelete.as_view(), name='delete_document')
]
