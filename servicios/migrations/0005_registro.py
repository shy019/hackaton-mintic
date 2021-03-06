# Generated by Django 3.2.7 on 2021-10-10 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_servicio_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=20)),
                ('edad', models.IntegerField(max_length=3)),
                ('ciudad', models.IntegerField(choices=[(1, 'Bogota'), (2, 'Medellín'), (3, '\tCali'), (4, 'Barranquilla'), (5, '\tCartagena de Indias'), (6, 'Soacha'), (7, 'Cúcuta'), (8, '\tSoledad'), (9, '\tBucaramanga'), (10, 'Bello'), (11, 'Villavicencio'), (12, 'Ibagué'), (13, 'Santa Marta'), (14, 'Valledupar'), (15, 'Manizales'), (16, 'Pereira'), (17, 'Montería'), (18, 'Neiva'), (19, 'Pasto'), (20, 'Armenia')], verbose_name='Ciudad')),
                ('elegir_evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
