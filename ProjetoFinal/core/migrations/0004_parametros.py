# Generated by Django 3.2.9 on 2021-11-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_veiculo_observacoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
