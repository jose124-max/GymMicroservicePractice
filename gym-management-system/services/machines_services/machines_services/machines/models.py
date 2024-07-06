# machines/models.py
from django.db import models

class Machine(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    url_imagen = models.URLField()

    def __str__(self):
        return self.nombre

