# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.DecimalField(decimal_places=0, max_digits=3)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=101)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=50)),
                ('horasPorSemana', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradoEducacion', models.CharField(choices=[('INF', 'Infantil'), ('PRM', 'Primaria'), ('ESO', 'Secundaria'), ('BAC', 'Bachillerato')], max_length=3)),
                ('curso', models.DecimalField(decimal_places=0, max_digits=1)),
                ('letra', models.CharField(blank=True, max_length=1)),
                ('asignaturas', models.ManyToManyField(to='setup.Asignatura')),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=101)),
                ('password', models.CharField(max_length=20)),
                ('asignaturaPrincipal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaturaPrincipal', to='setup.Asignatura')),
                ('asignaturaSecundaria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignaturaSecundaria', to='setup.Asignatura')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='clase',
            name='tutor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='setup.Profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.Clase'),
        ),
    ]