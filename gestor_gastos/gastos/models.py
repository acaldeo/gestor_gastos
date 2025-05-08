from django.db import models

class Quincena(models.Model):
    """
    Representa una quincena del mes.
    Por ejemplo: 'Quincena del 5', 'Quincena del 20'
    """
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


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
    """
    Registro de un gasto.
    Puede estar asociado a una quincena y tener un tipo: fijo o variable.
    """
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=10, choices=TipoGasto.choices)
    quincena = models.ForeignKey(Quincena, on_delete=models.CASCADE)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - ${self.monto}"


class Ingreso(models.Model):
    """
    Registro de ingreso (sueldo, transferencia, etc.)
    """
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    quincena = models.ForeignKey(Quincena, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"
