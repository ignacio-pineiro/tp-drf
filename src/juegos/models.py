from django.db import models

# Create your models here.

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo