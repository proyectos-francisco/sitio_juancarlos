# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import productos.models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20180828_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='original_file_name',
            field=models.CharField(default='test', editable=False, max_length=250, verbose_name='Nombre original'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to=productos.models.unique_file_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
    ]