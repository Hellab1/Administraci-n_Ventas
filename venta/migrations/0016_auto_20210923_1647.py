# Generated by Django 2.2.24 on 2021-09-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0015_auto_20210923_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cantidad',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='descripcion_productos',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='factura',
            name='forma_pago',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='neto',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='paquete',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='factura',
            name='piezas_paquete',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo_facturacion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo_pago',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]