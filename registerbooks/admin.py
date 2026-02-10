from django.contrib import admin
from .models import Autor, Editorial, Libro, Ejemplar


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombres", "apellidos")
    search_fields = ("nombres", "apellidos")
    ordering = ("apellidos", "nombres")

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
        "editorial",
        "edicion",
        "anio_publicacion",
        "clasificacion",
    )

    search_fields = (
        "titulo",
        "autor__nombres",
        "autor__apellidos",
        "editorial__nombre",
        "clasificacion",
    )

    list_filter = (
        "editorial",
        "clasificacion",
        "anio_publicacion",
    )

    ordering = ("titulo",)
    list_per_page = 25

    # 🚀 OPTIMIZACIÓN
    autocomplete_fields = ("autor", "editorial")
    list_select_related = ("autor", "editorial")


@admin.register(Ejemplar)
class EjemplarAdmin(admin.ModelAdmin):
    list_display = (
        "libro",
        "numero_ejemplar",
        "numero_registro",
        "disponible",
        "fecha_registro",
    )

    search_fields = (
        "libro__titulo",
        "numero_registro",
    )

    list_filter = (
        "disponible",
        "fecha_registro",
    )

    readonly_fields = ("fecha_registro",)
    autocomplete_fields = ("libro",)

    ordering = ("libro", "numero_ejemplar")
