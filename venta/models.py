from django.db import models

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
        return self.nombre_producto + ' ' + str(self.espesor) 

class Orden_Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    num_pedido = models.IntegerField()    
    fecha_compra = models.DateField()
    tipo_pago = models.CharField(max_length=50)
    forma_pago = models.CharField(max_length=30)
    tipo_facturacion = models.CharField(max_length=50)
    neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.num_pedido)

class Detalle_Venta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    total_detalle = models.IntegerField()
    orden_venta = models.ForeignKey(Orden_Compra, related_name='detalle', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto.nombre_producto + ' ' + str(self.producto.espesor) + 'mm'