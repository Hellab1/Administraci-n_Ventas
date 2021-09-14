from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Orden_Compra)
admin.site.register(Detalle_Venta)