from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from avaliacao.models import Avaliacao
from avaliacao.forms import AvaliacaoCreateForm

# Create your views here.
class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoCreateForm
    template_name = 'avaliacao/createavaliacao.html'


class AvaliacaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    context_object_name = 'avaliacao'
    template_name = "avaliacao/listnotas.html"



