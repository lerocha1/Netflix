
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Filme, Seriado
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

#def homepage(request):
#    return render(request, "homepage.html" )

class Homepage(TemplateView):
    template_name = 'homepage.html'

"""
def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all #aqui pegou todos os filmes do banco de dados usando a classe Filme
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)
"""
class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme #quando usa class para uma lista o padrão é object_lis, precisa trocar no html do filmes

class Detalhesfilme(DetailView):
    template_name = 'detalhefilmes.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super(Detalhesfilme, self).get(request, *args, **kwargs) #redireciona o usuario para uma url final

    def get_context_data(self, **kwargs):
        context =  super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes, pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria) [0:5]
        context["filmes_relacinados"] = filmes_relacionados
        return context

class Seriefilmes(ListView):
    template_name = "seriefilmes.html"
    model = Seriado

class Detalhesserie(DetailView):
    template_name = 'detalheseries.html'
    model = Seriado