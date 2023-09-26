from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from app.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('atores/', atores, name='atores/'),
    path('diretores/', diretores, name='diretores/'),

    path('filmes/', filmes, name='filmes'),

    path('series/', series, name='series'),
    path('episodios/', episodios, name='episodios'),
    path('temporadas/', temporadas, name='temporadas'),

    path('continentes/', continentes, name='continentes'),
    path('paises/', paises, name='paises'),
    path('generos/', generos, name = 'generos'),

    path('admin/', admin.site.urls),
]
