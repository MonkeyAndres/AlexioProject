# Generated by Django 2.0.1 on 2018-01-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0007_auto_20171210_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, default='static/alumnoPhotos/default-profile.png', upload_to='static/profesorPhotos/'),
        ),
    ]
