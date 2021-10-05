from rest_framework import serializers
from cms.models import PedidoModel

class ComprobanteSerializer(serializers.Serializer):
    pedidoId= serializers.IntegerField()
    tipoComprobante = serializers.ChoiceField(choices=['BOLETA','FACTURA'])
    numeroDocumento = serializers.CharField(min_length=8,max_length=11)

    def validate(self,data):
        '''Se llamara automaticamente cuando se llame al metodo is_valid() en el controlador'''
        try:
            data['pedidoId'] = PedidoModel.objects.filter(pedidoId = data.get('pedidoId')).first()
            
            if data.get('pedidoId') is None:
                raise Exception()
            return data

        except:
            raise serializers.ValidationError(detail='Error en el pedido')