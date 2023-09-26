from django.db import models


class Continente(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Pais(models.Model):
    nome = models.CharField(max_length=45)
    nacionalidade = models.CharField(max_length=60)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Diretor(models.Model):
    nome = models.CharField(max_length=45)
    site = models.CharField(max_length=60)
    instagram = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    twitter_x = models.CharField(max_length=30)
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Ator(models.Model):
    nome = models.CharField(max_length=45)
    site = models.CharField(max_length=60)
    instagram = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    twitter_x = models.CharField(max_length=30)
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Episodio(models.Model):
    nome = models.CharField(max_length=45)
    duracao_em_minutos = models.IntegerField()
    data_disponibilizacao = models.DateField()

    def __str__(self):
        return self.nome


class Temporada(models.Model):
    nome = models.CharField(max_length=45)
    episodios = models.ManyToManyField(Episodio)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    nome = models.CharField(max_length=45)
    duracao_em_minutos = models.IntegerField()
    sinopse = models.CharField(max_length=200)
    site_oficial = models.CharField(max_length=60)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(decimal_places=2, max_digits=5)
    generos = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    atores = models.ManyToManyField(Ator)

    def __str__(self):
        return self.nome


class Serie(models.Model):
    nome = models.CharField(max_length=45)
    duracao_em_minutos = models.IntegerField()
    sinopse = models.CharField(max_length=200)
    site_oficial = models.CharField(max_length=60)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(decimal_places=2, max_digits=5)
    generos = models.ManyToManyField(Genero)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    temporadas = models.ManyToManyField(Temporada)
