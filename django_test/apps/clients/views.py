# Create your views here.

from django.views.generic import DetailView, CreateView
from django.contrib import messages


from .models import Cliente
from .forms import CreateClientForm

class CreateClientView(CreateView):
	success_url = '/'
	template_name = "clients/crear.html" 
	model = Cliente
	form_class = CreateClientForm
	def form_valid(self, form):
		messages.add_message(self.request, messages.SUCCESS, 
				"Se creo el cliente!")

		return	super(CreateClientView, self).form_valid(form)

class DetailClientView(DetailView):
	model = Cliente
	template_name = "clients/ver.html"

	def get_context_data(self, **kwargs):
		context = super(DetailClientView, self).get_context_data(**kwargs)
		context.update({
			'hola': 'como estas'
			})
		return context