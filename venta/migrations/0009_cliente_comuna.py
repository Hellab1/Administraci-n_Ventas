# Generated by Django 2.2.24 on 2021-09-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0008_auto_20210903_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(default=122, on_delete=django.db.models.deletion.CASCADE, to='venta.Comuna'),
            preserve_default=False,
        ),
    ]