#para cada pagina precisa de 3 coisas
#url - view - template --- Sempre essas 3 coisas!
from django.urls import path
from .views import  Homefilmes, Homepage, Seriefilmes, Detalhesfilme


urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes', Homefilmes.as_view() ),
    path('serie', Seriefilmes.as_view()),
    path('filmes/<int:pk>',Detalhesfilme.as_view()),
    ]