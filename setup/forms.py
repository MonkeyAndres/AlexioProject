
from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'
        labels = {
            'concepto': _('Nombre Asignatura'),
            'horasPorSemana': _('Horas semanales asignatura'),
            'profesor': _('Profesor'),
            'curso': _('Curso'),
        }


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        exclude = ['username', 'password', 'token']
        labels = {
            'foto': _('Foto: Pulse aqui para añadir la foto.'),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        labels = {
            'gradoEducacion': _('Grado Educacion'),
            'anio': _('Año Curso (EJ: 1, 2)'),
            'letra': _('Letra Curso (EJ: A, B'),
        }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        exclude = ['username', 'password', 'token']
        labels = {
            'foto': _('Foto: Pulse aqui para añadir la foto.'),
        }
