# Generated by Django 2.2.24 on 2021-09-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0019_auto_20210924_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='num_paquete',
            field=models.CharField(default='prueba 1', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='paquetes',
            field=models.IntegerField(null=True),
        ),
    ]
