# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0009_auto_20171211_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='alumnosLeido',
            field=models.ManyToManyField(blank=True, to='setup.Alumno'),
        ),
    ]