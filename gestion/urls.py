
from django.urls import path
from .views import PruebaController, ProductoController, ProductosController,ClienteController,BuscadorClienteController,OperacionController,OperacionesController

urlpatterns=[
    path('prueba/',PruebaController.as_view()),
    path('productos/',ProductoController.as_view()),
    path('producto/<int:id>',ProductosController.as_view()),
    path('clientes/', ClienteController.as_view()),
    path('buscar-cliente/', BuscadorClienteController.as_view()),
    path('operacion/', OperacionController.as_view()),
    path('operacion/<int:id>', OperacionesController.as_view()),
]