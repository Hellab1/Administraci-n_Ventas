# Generated by Django 2.2.24 on 2021-09-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0012_auto_20210908_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='total_detalle',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]