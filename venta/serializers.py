from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import ReadOnlyField
from .models import Detalle_Venta, Factura

class detallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Venta
        fields = "__all__" 

class ventaSerializer(serializers.ModelSerializer):
    cliente_name = serializers.ReadOnlyField(source='cliente.nombre_cliente', read_only=True)
    cliente_rut = serializers.ReadOnlyField(source='cliente.rut_cliente', read_only=True)
    cliente_direccion = serializers.ReadOnlyField(source='cliente.direccion', read_only=True)
    detalles = detallesSerializer(many=True, read_only=True)

    class Meta:
        model = Factura
        fields = ('id_factura', 'codigo', 'n_pedido', 'fecha', 'cliente_rut', 'cliente_name', 'cliente_direccion',
        'detalles', 'neto', 'iva', 'total', 'tipo_pago', 'forma_pago', 'tipo_facturacion')
