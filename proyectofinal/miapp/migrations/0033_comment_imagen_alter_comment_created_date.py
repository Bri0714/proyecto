# Generated by Django 4.1.3 on 2022-12-13 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0032_ruta_conductor_alter_comment_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='Pruebas'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 10, 5, 32, 420047)),
        ),
    ]
