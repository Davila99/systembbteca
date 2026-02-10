from django.urls import path
from . import views

urlpatterns = [
    path("prestamo/<int:pk>/devolver/", views.devolver_prestamo),
]
