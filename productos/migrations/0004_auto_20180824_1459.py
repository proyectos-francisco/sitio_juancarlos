# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20180823_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to='fotos_productos', verbose_name='Imagen'),
        ),
    ]