# Generated by Django 3.2.9 on 2021-11-29 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_movrotativo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movrotativo',
            old_name='chackout',
            new_name='checkout',
        ),
    ]