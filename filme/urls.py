#para cada pagina precisa de 3 coisas
#url - view - template --- Sempre essas 3 coisas!
from django.urls import path
from .views import  Homefilmes, Homepage, Seriefilmes, Detalhesfilme, Detalhesserie

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes', Homefilmes.as_view(), name='homefilmes' ),
    path('serie', Seriefilmes.as_view(), name='seriefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('serie/<int:pk>', Detalhesserie.as_view(), name='detalhesserie')
    ]