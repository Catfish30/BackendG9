from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from .models import ProductoModel
from .serializers import ProductoSerializer

# Create your views here.

class PruebaController(APIView):
    def get(self,request,format=None):
        return Response(data={"message":"Exito"}, status=200)

    def post(self,request:Request,format=None):
        print(request.data)
        return Response(data={"message":"Hiciste post"})


class ProductoController(ListCreateAPIView):
    queryset = ProductoModel.objects.all() #SELECT * FROM productos;
    serializer_class = ProductoSerializer
