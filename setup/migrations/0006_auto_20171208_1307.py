# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_auto_20171206_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradoEducacion', models.CharField(choices=[('INF', 'Infantil'), ('PRM', 'Primaria'), ('ESO', 'Secundaria'), ('BAC', 'Bachillerato')], max_length=3)),
                ('anio', models.DecimalField(decimal_places=0, max_digits=1)),
                ('letra', models.CharField(blank=True, max_length=1)),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
            },
        ),
        migrations.RemoveField(
            model_name='clase',
            name='asignaturas',
        ),
        migrations.RemoveField(
            model_name='clase',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='asignaturaPrincipal',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='asignaturaSecundaria',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to='setup.Profesor'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, upload_to='static/alumnoPhotos/'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, upload_to='static/profesorPhotos/'),
        ),
        migrations.DeleteModel(
            name='Clase',
        ),
        migrations.AddField(
            model_name='curso',
            name='tutor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setup.Profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Curso'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='curso',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='clase', to='setup.Curso'),
        ),
    ]
