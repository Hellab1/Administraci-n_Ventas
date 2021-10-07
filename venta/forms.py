from django import forms

from .models import Crear_Factura, Orden_Compra, Detalle_Venta

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden_Compra
        fields = "__all__"

class DetalleForm(forms.ModelForm):

    class Meta:
        model = Detalle_Venta
        fields = ('id_detalle', 'cantidad', 'producto', 'num_paquete')

class crearForm(forms.ModelForm):

    class Meta:
        model = Crear_Factura
        fields = "__all__"