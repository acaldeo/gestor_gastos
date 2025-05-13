from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Quincena(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # obligatorio

    def __str__(self):
        return f"Quincena {self.fecha_inicio} - {self.fecha_fin}"


class Categoria(models.Model):
    """
    Categoría de un gasto, por ejemplo: 'Transporte', 'Servicios', 'Comida'
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoGasto(models.TextChoices):
    FIJO = 'fijo', 'Fijo'
    VARIABLE = 'variable', 'Variable'


class Gasto(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos')  # relación obligatoria

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"


class Ingreso(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # obligatorio
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"