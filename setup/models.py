
# DEFINICIONES DE MODELOS
from django.db import models


class Asignatura(models.Model):
    concepto = models.CharField(max_length=50)
    horasPorSemana = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self):
        return self.concepto


class Profesor(models.Model):
    foto = models.ImageField(blank=True)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    username = models.CharField(max_length=101)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40)

    asignaturaPrincipal = models.ForeignKey(
        Asignatura,
        related_name="asignaturaPrincipal"
    )
    asignaturaSecundaria = models.ForeignKey(
        Asignatura,
        blank=True,
        null=True,
        related_name="asignaturaSecundaria"
    )

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return self.nombre + " " + self.apellido


class Clase(models.Model):
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

    curso = models.DecimalField(max_digits=1, decimal_places=0)
    letra = models.CharField(max_length=1, blank=True)

    tutor = models.OneToOneField(Profesor)
    asignaturas = models.ManyToManyField(Asignatura)

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

    def __str__(self):
        cursoInt = str(self.curso)
        return cursoInt + "º" + self.letra


class Alumno(models.Model):
    foto = models.ImageField(blank=True)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DecimalField(max_digits=3, decimal_places=0)
    email = models.EmailField()

    username = models.CharField(max_length=101)
    password = models.CharField(max_length=20)
    token = models.CharField(max_length=40)

    clase = models.ForeignKey(Clase)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.clase.__str__()
