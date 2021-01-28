from django.db import models

# Create your models here.
class Lectura(models.Model):
    temperatura = models.CharField(max_length=180)
    humedad = models.CharField(max_length=300)
    luz = models.FloatField()

    def __str__(self):
        return f"Temperatura: {self.temperatura}° Humedad: {self.humedad}% Luz: {self.luz}"