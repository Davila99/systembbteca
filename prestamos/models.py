from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from registerbooks.models import Ejemplar


class Lector(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.PROTECT)
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.PROTECT)

    fecha_prestamo = models.DateField(default=timezone.now)
    fecha_devolucion_prevista = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ejemplar} → {self.lector}"

    def clean(self):
        # Solo validar cuando se crea el préstamo
        if self.pk is None and not self.ejemplar.disponible:
            raise ValidationError({
                "ejemplar": "Este ejemplar ya está prestado."
            })

    def save(self, *args, **kwargs):
        # Al crear el préstamo, marcar ejemplar como no disponible
        if self.pk is None and self.activo:
            self.ejemplar.disponible = False
            self.ejemplar.save()

        super().save(*args, **kwargs)

    def devolver(self):
        self.fecha_devolucion_real = timezone.now().date()
        self.activo = False
        self.ejemplar.disponible = True
        self.ejemplar.save()
        self.save()
