# Generated by Django 4.1 on 2023-12-04 10:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cesta', '0017_alter_pedido_secreto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='secreto',
            field=models.CharField(default=uuid.UUID('59b30c3c-e505-4084-ad6a-fb8091430f6b'), max_length=255),
        ),
    ]
