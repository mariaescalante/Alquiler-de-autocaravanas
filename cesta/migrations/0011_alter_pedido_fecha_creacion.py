# Generated by Django 4.1 on 2023-11-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cesta', '0010_pedido_estado_pedido_fecha_creacion_pedido_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
