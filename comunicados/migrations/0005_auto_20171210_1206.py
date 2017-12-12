# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_auto_20171208_1307'),
        ('comunicados', '0004_auto_20171208_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='asignatura',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Asignatura'),
        ),
        migrations.RemoveField(
            model_name='comunicado',
            name='receptor',
        ),
        migrations.AddField(
            model_name='comunicado',
            name='receptor',
            field=models.ManyToManyField(default=True, to='setup.Curso'),
        ),
    ]
