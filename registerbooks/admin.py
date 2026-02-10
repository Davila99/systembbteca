from django.contrib import admin
from .models import Autor, Categoria, Editorial, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos")
    search_fields = ("nombres", "apellidos")
    ordering = ("apellidos", "nombres")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "lugar_publicacion")
    search_fields = ("nombre", "lugar_publicacion")
    ordering = ("nombre",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "categoria",
        "editorial",
        "edicion",
        "anio_publicacion",
        "clasificacion",
    )

    search_fields = (
        "titulo",
        "autor__nombres",
        "autor__apellidos",
        "categoria__nombre",
        "editorial__nombre",
        "edicion",
        "clasificacion",
    )

    list_filter = (
        "categoria",
        "autor",
        "editorial",
        "anio_publicacion",
    )

    ordering = ("-anio_publicacion",)
    list_per_page = 25
