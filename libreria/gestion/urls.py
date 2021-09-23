
from django.urls.resolvers import URLPattern

from django.urls import path
from .views import PruebaController, ProductoController

urlpatterns=[
    path('prueba/',PruebaController.as_view()),
    path('productos/',ProductoController.as_view())
]