from django import forms

from .models import Orden_Compra

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden_Compra
        fields = "__all__"