# Generated by Django 5.2 on 2025-05-10 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0002_remove_gasto_nombre_remove_gasto_pagado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='quincena',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingresos', to='gastos.quincena'),
        ),
    ]
