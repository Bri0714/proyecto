# Generated by Django 4.1.3 on 2022-12-13 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0026_alter_comment_created_date_alter_ruta_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 56, 0, 154277)),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='number',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='placa',
            field=models.CharField(default='1', max_length=40),
        ),
    ]
