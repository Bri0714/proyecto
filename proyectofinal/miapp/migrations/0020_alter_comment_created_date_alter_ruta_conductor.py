# Generated by Django 4.1.3 on 2022-12-13 03:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0019_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 22, 0, 10, 390068)),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='conductor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='miapp.conductor'),
        ),
    ]
