from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Prestamo


def devolver_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    prestamo.devolver()
    messages.success(request, "Préstamo devuelto correctamente.")
    return redirect("/admin/prestamos/prestamo/")
