# Generated by Django 5.2 on 2025-05-10 23:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0004_alter_gasto_categoria_alter_gasto_descripcion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingreso',
            name='fuente',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='quincena',
        ),
        migrations.AddField(
            model_name='ingreso',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gastos.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingreso',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
