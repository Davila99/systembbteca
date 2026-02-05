from django.contrib import admin
from .models import Autor, Categoria, Libro
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "nacionalidad")
    search_fields = ("nombre", "apellido", "nacionalidad")
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "categoria",
        "isbn",
        "fecha_publicacion",
        "disponible",
    )
    search_fields = (
        "titulo",
        "isbn",
        "autor__nombre",
        "autor__apellido",
        "categoria__nombre",
    )
    list_filter = (
        "categoria",
        "autor",
        "disponible",
        "fecha_publicacion",
    )
    date_hierarchy = "fecha_publicacion"
