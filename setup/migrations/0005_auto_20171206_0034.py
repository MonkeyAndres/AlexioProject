# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0004_auto_20171014_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, upload_to='alumnoPhotos/'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, upload_to='profesorPhotos/'),
        ),
    ]
