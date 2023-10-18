#para cada pagina precisa de 3 coisas
#url - view - template --- Sempre essas 3 coisas!
from django.urls import path
from .views import  homefilmes, Homepage


urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes', homefilmes ),
    ]