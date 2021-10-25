from django import forms

from .models import *

class facturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = ('id_factura', 'codigo', 'n_pedido', 'fecha', 'tipo_pago', 'forma_pago', 'tipo_facturacion', 'cliente')

class DetalleForm(forms.ModelForm):

    class Meta:
        model = Detalle_Venta
        fields = ('id_detalle', 'cantidad', 'num_paquete', 'producto')
