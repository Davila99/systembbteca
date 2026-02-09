from django.db import models

from django.db import models

class Autor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
class Editorial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    lugar_publicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    edicion = models.CharField(max_length=20)
    anio_publicacion = models.PositiveIntegerField()
    clasificacion = models.CharField(max_length=50)  # Ej: 658.151 G5861

    def __str__(self):
        return self.titulo

class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    numero_registro = models.CharField(max_length=50, unique=True)
    numero_ejemplar = models.PositiveIntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.libro.titulo} - Ejemplar {self.numero_ejemplar}"
