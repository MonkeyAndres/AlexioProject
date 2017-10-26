
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
        }


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        exclude = ['username', 'password', 'token']
        labels = {
            'asignaturaPrincipal': _('Asignatura Principal'),
            'asignaturaSecundaria': _('Asignatura Secundaria (no requerida)'),
        }


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        labels = {
            'gradoEducacion': _('Grado Educacion'),
            'curso': _('Año Curso (EJ: 1, 2)'),
            'letra': _('Letra Curso (EJ: A, B'),
            'asignaturas': _('Asignaturas que cursa la clase'),
        }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        exclude = ['username', 'password', 'token']
