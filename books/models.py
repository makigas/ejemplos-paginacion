from django.db import models


class Book(models.Model):
    name = models.CharField('Nombre', max_length=64)
    author = models.CharField('Autor', max_length=64)
    year = models.CharField('Año', max_length=8)
    isbn = models.CharField('ISBN', max_length=64)
    created_at = models.DateTimeField()
