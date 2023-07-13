from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre=models.CharField()
    autor=models.CharField()
    codigo=models.CharField()
    estado=models.CharField(max_length=2)
    def _str_(self):
        return'Libro: {self.nombre}'

class Compra(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.libro.nombre} - {self.fecha}"
