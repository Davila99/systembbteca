from django.contrib import admin
from .models import Autor, Categoria, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "apellido", "nacionalidad")
    search_fields = ("nombre", "apellido", "nacionalidad")
    list_filter = ("nacionalidad",)
    ordering = ("apellido", "nombre")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("nombre",)


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
        "disponible",          # Sí / No
        "categoria",           # Por categoría
        "autor",               # Por autor
        "fecha_publicacion",   # Por año/mes
    )

    date_hierarchy = "fecha_publicacion"
    list_per_page = 25
    ordering = ("-fecha_publicacion",)
