# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0011_documentocomunicado_nombredocumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentocomunicado',
            name='file',
            field=models.FileField(upload_to='static/documents'),
        ),
    ]