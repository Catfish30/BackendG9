from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import ProductoModel
from .serializers import ProductoSerializer
from rest_framework import status

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

    def get(self, request):
        respuesta = self.queryset.filter(productoEstado = True).all()
        print(respuesta)
        respuesta_serializada =self.serializer_class(instance=respuesta, many=True)
        return Response(data={
            "message":None,
            "content": respuesta_serializada.data
        })

    def post(self, request:Request):
        print(request.data)
        data = self.serializer_class(data=request.data)
        # data.is_valid(raise_exception=True)
        if data.is_valid():
            data.save()
            return Response(data={
            "message":"Producto creado Exitosamente",
            "content":data.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al guardar Producto",
                "content":data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class ProductosController(APIView):

    def get(self, request, id):
        print(id)
        productoEncontrado = ProductoModel.objects.filter(productoId = id)
        print(productoEncontrado)
        try:
            productoEncontrado2 = ProductoModel.objects.get(productoId = id)
            print(productoEncontrado2)
        except ProductoModel.DoesNotExist:
            print('No se encontro')

        if productoEncontrado2 is None:
            return Response(data={
            "message":"Producto no encontrado",
            "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(instance=productoEncontrado2)

        return Response(data={
            "message":None,
            "content": serializador.data
        })
    def put(self, request, id):

        productoEncontrado = ProductoModel.objects.filter(productoId = id).first()
        if productoEncontrado is None:
            return Response(data={
                "message":"Producto no encontrado",
                "content":None
            },status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=productoEncontrado, validated_data=serializador.validated_data)

            return Response(data={
                "message":"Producto actualizado exitosamente",
                "content":serializador.data
            })
        else:
            return Response(data={
                "message":"Error al actualizar producto",
                "content":serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        productoEncontrado: ProductoModel = ProductoModel.objects.filter(productoId = id).first()

        if productoEncontrado is None:
            return Response(data={
                "message":"Producto no encontrado",
                "content":None
            },status=status.HTTP_404_NOT_FOUND)

        productoEncontrado.productoEstado = False
        productoEncontrado.save()

        serializador = ProductoSerializer(instance=productoEncontrado)

        return Response(data={
            "message":"Producto eliminado exitosamente",
            "content":serializador.data
        })
