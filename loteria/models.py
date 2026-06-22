from django.db import models

# Create your models here.
from django.db import models

# La clase RegistroLoteria representa una tabla en la base de datos.
# Cada instancia de esta clase = una fila en esa tabla.
class RegistroLoteria(models.Model):

    # Campo para el número de lotería (entero positivo)
    numero = models.PositiveIntegerField(
        verbose_name="Número de Lotería"
    )

    # Campo para la fecha del sorteo
    fecha = models.DateField(
        verbose_name="Fecha del Sorteo"
    )

    # Este método controla cómo se muestra el objeto en texto
    def __str__(self):
        return f"Número {self.numero} - {self.fecha}"
