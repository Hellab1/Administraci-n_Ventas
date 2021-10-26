from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
    
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=12)
    nombre_cliente = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=64)
    region = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre_cliente

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    espesor = models.IntegerField()
    tipo = models.BooleanField()
    precio_neto = models.IntegerField()

    def __str__(self):
        return self.nombre_producto + ' ' + str(self.espesor) + 'mm'

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    n_pedido = models.IntegerField()
    fecha = models.DateField()
    neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    tipo_pago = models.CharField(max_length=50)
    forma_pago = models.CharField(max_length=30)
    tipo_facturacion = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Detalle_Venta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    total_detalle = models.IntegerField()
    piezas_paquete = models.IntegerField()
    num_paquete = models.CharField(max_length=45)
    orden_venta = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='detalles', on_delete=models.CASCADE)