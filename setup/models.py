
# DEFINICIONES DE MODELOS
from django.db import models


class Profesor(models.Model):
    foto = models.ImageField(blank=True, upload_to="static/profesorPhotos/", default="static/alumnoPhotos/default-profile.png  ")

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    username = models.CharField(max_length=101)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre + " " + self.apellido


class Curso(models.Model):
    gradoEducacionChoices = (
        ('INF', 'Infantil'),
        ('PRM', 'Primaria'),
        ('ESO', 'Secundaria'),
        ('BAC', 'Bachillerato'),
    )

    gradoEducacion = models.CharField(
        max_length=3,
        choices=gradoEducacionChoices
    )

    anio = models.DecimalField(max_digits=1, decimal_places=0)
    letra = models.CharField(max_length=1, blank=True)

    tutor = models.OneToOneField(Profesor)

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

    def __str__(self):
        anioInt = str(self.anio)
        return anioInt + "º" + self.letra


class Asignatura(models.Model):
    concepto = models.CharField(max_length=50)
    horasPorSemana = models.DecimalField(max_digits=2, decimal_places=0)
    profesor = models.ForeignKey(
        Profesor,
        related_name="profesor",
        default=True
    )
    curso = models.ForeignKey(
        Curso,
        related_name="clase",
        default=True
    )

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self):
        return self.concepto + " - " + self.curso.__str__()


class Alumno(models.Model):
    foto = models.ImageField(blank=True, upload_to="static/alumnoPhotos/", default="static/alumnoPhotos/default-profile.png  ")

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DecimalField(max_digits=3, decimal_places=0)
    email = models.EmailField()

    username = models.CharField(max_length=101)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40)

    curso = models.ForeignKey(Curso, default=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.curso.__str__()
