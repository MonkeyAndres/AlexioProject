from django.db import models
from setup.models import *


class Comunicado(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    emisor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(
        Asignatura,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    receptores = models.ManyToManyField(Curso, default=True)
    alumnosLeido = models.ManyToManyField(Alumno, blank=True)

    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"

    def __str__(self):
        return self.titulo + " - " + self.emisor.__str__()


class DocumentoComunicado(models.Model):
    nombreDocumento = models.CharField(max_length=255, default="NombreArchivo")
    file = models.FileField(upload_to="static/documents")
    comunicado = models.ForeignKey(
        Comunicado,
        related_name="documentos",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Documento Comunicado"
        verbose_name_plural = "Documento Comunicados"

    def __str__(self):
        return self.nombreDocumento
