# Generated by Django 2.0.1 on 2018-01-25 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunicados', '0013_auto_20171211_1020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DocumentoComunicado',
            new_name='AdjuntoComunicado',
        ),
    ]
