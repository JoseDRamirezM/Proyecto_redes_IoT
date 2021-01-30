from django.db import models

# Create your models here.
class Lectura(models.Model):
    temperatura = models.CharField(max_length=10)
    humedad = models.CharField(max_length=10)
    intensidad_luz = models.FloatField(max_length=10)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Temperatura: {self.temperatura}° Humedad: {self.humedad}% Luz: {self.intensidad_luz} Fecha: {self.datetime}"