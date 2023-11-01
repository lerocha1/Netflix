from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criação') #esse menos é o mesmo que desc em SQL
    return{"lista_filmes_recentes" : lista_filmes}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_emalta" : lista_filmes}