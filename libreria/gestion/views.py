from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .models import CabeceraModel, DetalleModel, ProductoModel, ClienteModel
from .serializers import ProductoSerializer,ClienteSerializer,OperacionSerializer,OperacionModelSerializer
from rest_framework import status
from .utils import PaginacionPersonalizada
from rest_framework.serializers import Serializer
import requests as solicitudes
from os import environ
from django.db.models.query import QuerySet
from django.db import transaction,Error
from datetime import datetime

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
    pagination_class = PaginacionPersonalizada


    # def get(self, request):
    #     respuesta = self.queryset.filter(productoEstado = True).all()
    #     print(respuesta)
    #     respuesta_serializada =self.serializer_class(instance=respuesta, many=True)
    #     return Response(data={
    #         "message":None,
    #         "content": respuesta_serializada.data
    #     })

    def post(self, request:Request):
        # print(request.data)
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
        # print(id)
        productoEncontrado = ProductoModel.objects.filter(productoId = id)
        # print(productoEncontrado)
        try:
            productoEncontrado2 = ProductoModel.objects.get(productoId = id)
            # print(productoEncontrado2)
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

class ClienteController(CreateAPIView):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer


    def post(self, request: Request):

        data: Serializer = self.get_serializer(data=request.data)
        if data.is_valid():

            documento = data.validated_data.get('clienteDocumento')
            direccion = data.validated_data.get('clienteDireccion')

            url = 'https://apiperu.dev/api/'
            if len(documento) == 8:
                

                if direccion is None:
                    return Response(data={
                        'message': 'Clientes con DNI debe proveer la direccion'
                    }, status=status.HTTP_400_BAD_REQUEST)
                url +='dni/'

            elif len(documento) == 11:
                url +='ruc/'

            resultado = solicitudes.get(url+documento, headers={
                'Contente-Type':'application/json',
                'Authorization':'Bearer '+environ.get('APIPERU_TOKEN')
            })
            print(resultado.json())
            success = resultado.json().get('success')

            if success is False:
                return Response(data={
                'message': 'Documento Incorrecto'
            }, status=status.HTTP_400_BAD_REQUEST)

            data = resultado.json().get('data')
            nombre = data.get('nombre_completo') if data.get('nombre_completo') else data.get('nombre_o_razon_social')
            print(nombre)

            direccion = direccion if len(documento) == 8 else data.get('direccion_completa')
            print(direccion)

            nuevoCliente = ClienteModel(
                clienteNombre =nombre,clienteDocumento = documento, clienteDireccion=direccion
            )

            nuevoCliente.save()

            nuevoClienteSerializado: Serializer = self.serializer_class(instance=nuevoCliente)

            # print(data.validated_data)
            return Response(data={
                'message': 'Cliente agregado exitosamente',
                "content": nuevoClienteSerializado.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al ingresar el cliente',
                'content': data.errors
            },status=status.HTTP_400_BAD_REQUEST)

class BuscadorClienteController(RetrieveAPIView):

    serializer_class = ClienteSerializer
    def get(self, request: Request):
        print(request.query_params)

        documento = request.query_params.get('documento')
        nombre = request.query_params.get('nombre')
        clienteEncontrado =None

        if documento:
            clienteEncontrado : QuerySet = ClienteModel.objects.filter(clienteDocumento=documento)
            # if clienteEncontrado is None:
            #     return Response({
            #         'message':'Cliente no existe',
            #     }, status=status.HTTP_404_NOT_FOUND)
            
            data = self.serializer_class(instance=clienteEncontrado,many=True)

            # return Response({'content': data.data})

        if nombre:

            if clienteEncontrado is not None:

                clientesEncontrado = clienteEncontrado.filter(clienteNombre__icontains=nombre).all()
            else:
                clientesEncontrado = ClienteModel.objects.filter(clienteNombre__icontains=nombre).all()

        data = self.serializer_class(instance=clienteEncontrado,many=True)
        #1. agregar test para el cliente controler y su busqueda. 2. dar opcion que se pueda enviar documento y nombre a la vez y se haga el filtro de ambos si se provee
        return Response(data={
            'message':'Los usuarios son:',
            'content':data.data
        })

        # return Response({'message':None})

class OperacionController(CreateAPIView):
    serializer_class= OperacionSerializer
    def post(self,request:Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():

            documento =data.validated_data.get('cliente')
            clienteEncontrado = ClienteModel.objects.filter(clienteDocumento=documento).first()
            print(clienteEncontrado)
            detalles = data.validated_data.get('detalle')
            tipo = data.validated_data.get('tipo')
            try:
                with transaction.atomic():
                    if clienteEncontrado is None:
                        raise Error('Usuario no existe')
                    nuevaCabecera = CabeceraModel(cabeceraTipo=tipo,clientes = clienteEncontrado)
                    nuevaCabecera.save()
                    for detalle in detalles:
                        producto = ProductoModel.objects.get(productoId = detalle.get('producto'))
                        DetalleModel(detalleCantidad= detalle.get('cantidad'),
                            detalleImporte=producto.productoPrecio*detalle.get('cantidad'),
                            productos=producto, 
                            cabeceras=nuevaCabecera).save()
            except Error as e:
                print(e)
                return Response(data={
                    'message':'Error al crear la operacion',
                    'content':e.args
                })
            except Exception as exc:
                return Response(data={
                     'message':'Error al crear la operacion',
                     'content':exc.args
                })
            return Response(data={
                'message':'Operacion registrada exitosamente'
            })

        else:
            return Response(data={
                'message':'Error al crear la operacion',
                'content':data.errors
            },status=status.HTTP_400_BAD_REQUEST)

class OperacionesController(RetrieveAPIView):
    serializer_class = OperacionModelSerializer
    def get(self,request: Request,id):
        cabecera = get_object_or_404(CabeceraModel,pk =id)
        # cabecera = CabeceraModel.objects.get(cabeceraId=id)
        print(cabecera)
        cabecera_serializada = self.serializer_class(instance=cabecera)
        return Response(data={
            'message':'La operacion es:',
            'content':cabecera_serializada.data
        })