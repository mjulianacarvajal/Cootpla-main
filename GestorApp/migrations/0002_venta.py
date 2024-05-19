# Generated by Django 4.2.7 on 2024-05-14 14:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_compra', models.CharField(max_length=100)),
                ('comprador', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('asientos_compra', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('estado', models.CharField(choices=[('1', 'Hecho'), ('0', 'Cancelado')], default='1', max_length=1, verbose_name='Estado')),
                ('fecha_creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True)),
                ('programacion_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestorApp.programacion')),
            ],
        ),
    ]