# Generated by Django 3.2.9 on 2021-11-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_empregado_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(upload_to='cliente_fotos'),
        ),
    ]
