from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView

# Create your views here.

#def homepage(request):
#    return render(request, "homepage.html" )

class Homepage(TemplateView):
    template_name = 'homepage.html'


def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all #aqui pegou todos os filmes do banco de dados usando a classe Filme
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)
