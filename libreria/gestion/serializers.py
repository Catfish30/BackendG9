from django.db.models import fields
from rest_framework import serializers
from .models import ProductoModel,ClienteModel

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