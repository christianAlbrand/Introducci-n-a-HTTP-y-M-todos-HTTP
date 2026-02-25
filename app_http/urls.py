# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.obtener_productos),
    path("productos/crear/", views.crear_producto),
    path("productos/actualizar/<int:id>/", views.actualizar_producto),
    path("productos/eliminar/<int:id>/", views.eliminar_producto),
]