from django.views.generic import CreateView
from .models import Documento

class DocumentoNovo(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        #self.pk_url_kwarg = self.kwargs['funcionario_id']
        #self.slug_url_kwarg = self.kwargs['funcionario_id']
        #self.pk_url_kwarg = 'pk'
        #self.slug_url_kwargs = {'slug': 'funcionario_id'}
        #self.object = self.get_object()

        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

