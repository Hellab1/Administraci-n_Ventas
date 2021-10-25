from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import ReadOnlyField
from .models import Detalle_Venta, Factura, Producto

class ventaSerializer(serializers.ModelSerializer):
    cliente_name = serializers.ReadOnlyField(source='cliente.nombre_cliente', read_only=True)
    cliente_rut = serializers.ReadOnlyField(source='cliente.rut_cliente', read_only=True)
    cliente_direccion = serializers.ReadOnlyField(source='cliente.direccion', read_only=True)
    cliente_comuna = serializers.ReadOnlyField(source='cliente.comuna', read_only=True)
    cliente_region = serializers.ReadOnlyField(source='cliente.region', read_only=True)
    detalle = serializers.StringRelatedField(many=True)

    class Meta:
        model = Factura
        fields = ('id_compra', 'num_pedido', 'fecha_compra', 'cliente_rut', 'cliente_name', 'cliente_direccion', 'cliente_comuna',
        'cliente_region', 'detalle', 'neto', 'iva', 'total', 'tipo_pago', 'forma_pago', 'tipo_facturacion')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre_producto')

class ordenDetalleSerializer(serializers.ModelSerializer):
    productos = productoSerializer(many=True, read_only=True)
    class Meta:
        model = Detalle_Venta
        fields = ('productos')

class detallesSerializer(serializers.ModelSerializer):
    cliente_name = serializers.ReadOnlyField(source='cliente.nombre_cliente', read_only=True)
    productos = ordenDetalleSerializer(many=True, read_only=True)
    class Meta:
        model = Factura
        fields = ('cliente_name', 'id_compra', 'num_pedido', 'tipo_pago', 'productos')