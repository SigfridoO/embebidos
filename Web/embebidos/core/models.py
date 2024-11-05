from django.db import models

class Memoria(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="titulo")
    subtitulo = models.CharField(max_length=100, verbose_name="subtitulo")
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    resumen = models.CharField(max_length=400, verbose_name="resumen")
    contenido = models.CharField(max_length=1000, verbose_name="contenido")
    imagen = models.ImageField(verbose_name="imagen", upload_to="pasajes", default="")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name = "Memoria"
        verbose_name_plural = "Memorias"
        ordering = ['-creado']

    def __str__(self):
        return self.titulo