# Generated by Django 4.0 on 2021-12-27 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadas', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=256)),
                ('estado', models.CharField(max_length=2)),
                ('curso_agua', models.CharField(max_length=256)),
                ('codigo', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('croqui', models.CharField(max_length=256)),
                ('titulo', models.CharField(choices=[('PR', 'Proprietário'), ('PO', 'Posseiro'), ('AS', 'Assentado'), ('AR', 'Arrendatário'), ('PA', 'Parceiro'), ('US', 'Usufruário'), ('SU', 'Processo sucessório em andamento'), ('PM', 'Participação da mulher na gestão')], default='PR', max_length=2)),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiario', to='sistema.pessoa')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colaborador', to='sistema.pessoa')),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.localizacao')),
            ],
        ),
    ]
