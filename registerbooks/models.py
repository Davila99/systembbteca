from django.db import models
from django.core.validators import MinValueValidator
from datetime import date


class Autor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    class Meta:
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Editorial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    lugar_publicacion = models.CharField(max_length=100)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="libros"
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        related_name="libros"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="libros"
    )
    edicion = models.CharField(max_length=20)
    anio_publicacion = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1500)]
    )
    clasificacion = models.CharField(
    max_length=50,
    null=True,
    blank=True
)
    class Meta:
        ordering = ["-anio_publicacion", "titulo"]

    def __str__(self):
        return self.titulo


class Ejemplar(models.Model):
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="ejemplares"
    )
    numero_registro = models.CharField(max_length=50, unique=True)
    numero_ejemplar = models.PositiveIntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["libro", "numero_ejemplar"]
        unique_together = ("libro", "numero_ejemplar")

    def __str__(self):
        return f"{self.libro.titulo} - Ejemplar {self.numero_ejemplar}"
