# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_auto_20171208_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, default='static/alumnoPhotos/default-profile.png  ', upload_to='static/alumnoPhotos/'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, default='static/alumnoPhotos/default-profile.png  ', upload_to='static/profesorPhotos/'),
        ),
    ]
