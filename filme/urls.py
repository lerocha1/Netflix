#para cada pagina precisa de 3 coisas
#url - view - template --- Sempre essas 3 coisas!
from django.urls import path, include
from .views import homepage


urlpatterns = [
    path('', homepage),
]