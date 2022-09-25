from django.conf.urls import url
from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo,
    Pdf,
    PdfDebug
)
from .views import pdf_reportlab

urlpatterns = [
    path('funcionarios', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('pdf-reportlab', pdf_reportlab, name='pdf_reportlab'),
    path('relatorio_funcionario_html', Pdf.as_view(), name='relatorio_funcionario_html'),
    path('relatorio_funcionario_html_debug', PdfDebug.as_view(), name='relatorio_funcionario_html_debug')
]
