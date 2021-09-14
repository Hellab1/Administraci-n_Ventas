from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Orden_Compra

class ventaSerializer(serializers.ModelSerializer):
    cliente_name = serializers.ReadOnlyField(source='cliente.nombre_cliente', read_only=True)
    cliente_rut = serializers.ReadOnlyField(source='cliente.rut_cliente', read_only=True)
    cliente_direccion = serializers.ReadOnlyField(source='cliente.direccion', read_only=True)
    cliente_comuna = serializers.ReadOnlyField(source='cliente.comuna', read_only=True)
    cliente_region = serializers.ReadOnlyField(source='cliente.region', read_only=True)
    detalle = serializers.StringRelatedField(many=True)

    class Meta:
        model = Orden_Compra
        fields = ('id_compra', 'num_pedido', 'fecha_compra', 'cliente_rut', 'cliente_name', 'cliente_direccion', 'cliente_comuna',
        'cliente_region', 'detalle', 'neto', 'iva', 'total', 'tipo_pago', 'forma_pago', 'tipo_facturacion')

class detallesSerializer(serializers.ModelSerializer):
    cliente_name = serializers.ReadOnlyField(source='cliente.nombre_cliemte', read_only=True)
    productos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Orden_Compra
        fields = ('id_compra', 'num_pedido', 'tipo_pago', 'productos', 'cliente_name')