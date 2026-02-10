from django.contrib import admin
from .models import Lector, Prestamo


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombres", "apellidos", "telefono")
    search_fields = ("cedula", "nombres", "apellidos")


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        "lector",
        "ejemplar",
        "fecha_prestamo",
        "fecha_devolucion_prevista",
        "activo",
    )
    list_filter = ("activo",)
    search_fields = (
        "lector__nombres",
        "lector__apellidos",
        "ejemplar__libro__titulo",
    )
