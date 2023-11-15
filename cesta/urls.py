from django.urls import path
from .views import agregar_al_carrito, ver_carrito

urlpatterns = [
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
]