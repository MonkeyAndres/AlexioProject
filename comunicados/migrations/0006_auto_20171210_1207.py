# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0005_auto_20171210_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Asignatura'),
        ),
    ]
