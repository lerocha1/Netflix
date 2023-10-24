from django.contrib import admin
from .models import Filme, Seriado, Usuario, Episodio

# Register your models here.
admin.site.register(Filme)
admin.site.register(Seriado)
admin.site.register(Usuario)
admin.site.register(Episodio)