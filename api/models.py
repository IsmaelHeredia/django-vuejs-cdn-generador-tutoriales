from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length = 180)
    afinacion = models.CharField(max_length = 180)
    dificultad = models.CharField(max_length = 180, default='')
    link_youtube = models.CharField(max_length = 180)
    fecha = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.titulo

class CapturaCancion(models.Model):
    cancion = models.ForeignKey(Cancion,on_delete=models.CASCADE,default=0)
    descripcion = models.CharField(max_length = 180)
    imagen = models.CharField(max_length = 180)
    orden = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.descripcion
