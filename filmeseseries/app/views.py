from django.shortcuts import render
from app.models import *


def atores(request):
    consulta = {
        'atores': Ator.objects.all()
    }

    return render(request, 'pessoas/atores.html', consulta)


def diretores(request):
    consulta = {
        'diretores': Diretor.objects.all()
    }

    return render(request, 'pessoas/diretores.html', consulta)


def continentes(request):
    consulta = {
        'continentes': Continente.objects.all()
    }

    return render(request, 'informacao/continentes.html', consulta)


def paises(request):
    consulta = {
        'paises': Pais.objects.all()
    }

    return render(request, 'informacao/paises.html', consulta)


def generos(request):
    consulta = {
        'generos': Genero.objects.all()
    }

    return render(request, 'informacao/generos.html', consulta)


def filmes(request):
    consulta = {
        'filmes': Filme.objects.all()
    }

    return render(request, 'filmes/filmes.html', consulta)


def episodios(request):
    consulta = {
        'episodios': Episodio.objects.all()
    }

    return render(request, 'series/episodios.html', consulta)


def temporadas(request):
    consulta = {
        'temporadas': Temporada.objects.all()
    }

    return render(request, 'series/temporadas.html', consulta)


def series(request):
    consulta = {
        'series': Serie.objects.all()
    }

    return render(request, 'series/series.html', consulta)
