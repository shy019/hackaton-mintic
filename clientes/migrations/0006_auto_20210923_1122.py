# Generated by Django 3.2.7 on 2021-09-23 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_factura'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'verbose_name': 'factura', 'verbose_name_plural': 'facturas'},
        ),
        migrations.AddField(
            model_name='factura',
            name='dueño_vehiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
        migrations.AddField(
            model_name='factura',
            name='precio_estadar_tipo_vehiculo',
            field=models.IntegerField(choices=[(1, '4000'), (2, '4000'), (3, '3500'), (4, '2000'), (5, '5000'), (6, '8000')], null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='hora_llegada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='hora_salida',
            field=models.DateTimeField(),
        ),
    ]
