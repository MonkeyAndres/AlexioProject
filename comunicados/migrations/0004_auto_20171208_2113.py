# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 21:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0003_auto_20171208_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunicado',
            old_name='receptores',
            new_name='receptor',
        ),
    ]
