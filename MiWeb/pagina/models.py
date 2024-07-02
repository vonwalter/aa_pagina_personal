from django.db import models

class Index(models.Model):
    nombre = models.CharField(max_length=100)
    foto_de_fondo = models.ImageField(upload_to='fondo/')
    mi_foto = models.ImageField(upload_to='fotos/')
    soy_1 = models.CharField(max_length=100)
    soy_2 = models.CharField(max_length=100)
    soy_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre