from django.db.models import fields
from django.test import client
from rest_framework import serializers
from .models import DetalleModel, ProductoModel,ClienteModel,CabeceraModel

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoModel

        fields = '__all__'

        # exclude = ['productoId']

class ClienteSerializer(serializers.ModelSerializer):

    clienteNombre = serializers.CharField(max_length=45,required=False,trim_whitespace=True,read_only=True)
    clienteDireccion = serializers.CharField(max_length=100,required=False,trim_whitespace=True)
    # clienteGenero = serializers.CharField(max_length=10,required=True)

    class Meta:
        model = ClienteModel
        fields = '__all__'


class DetalleOperacionSerializer(serializers.Serializer):

    cantidad = serializers.IntegerField(required=True,min_value=1)

    importe = serializers.DecimalField(max_digits=5,decimal_places=2,min_value=0.01,required=True)
    
    producto = serializers.IntegerField(required=True,min_value=1)

class OperacionSerializer(serializers.Serializer):

    tipo = serializers.ChoiceField(choices=[('V','VENTA'),('C','COMPRA')], required=True)

    cliente = serializers.IntegerField(required=True, min_value=1)

    detalle = DetalleOperacionSerializer(many=True)

class DetalleOperacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleModel
        # fields = '__all__'
        exclude = ['cabeceras']
        depth = 1
class OperacionModelSerializer(serializers.ModelSerializer):
    cabeceraDetalles = DetalleOperacionModelSerializer(many=True)

    class Meta:
        model = CabeceraModel
        fields = '__all__'
        depth = 1
