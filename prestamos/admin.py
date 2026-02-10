from django.contrib import admin
from django.utils.html import format_html
from .models import Lector, Prestamo


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombres", "apellidos")
    search_fields = ("cedula", "nombres", "apellidos")


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        "lector",
        "ejemplar",
        "fecha_prestamo",
        "fecha_devolucion_prevista",
        "activo",
        "accion_devolver",
    )
    list_filter = ("activo",)
    search_fields = (
        "lector__nombres",
        "lector__apellidos",
        "ejemplar__libro__titulo",
    )

    def accion_devolver(self, obj):
        if obj.activo:
            return format_html(
                '<a class="button" href="/admin/prestamos/prestamo/{}/devolver/">Devolver</a>',
                obj.id
            )
        return "—"

    accion_devolver.short_description = "Acción"
