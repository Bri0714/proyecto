# Generated by Django 4.1.3 on 2022-12-13 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0033_comment_imagen_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='images/Pruebas'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 12, 15, 43, 394263)),
        ),
    ]
