from django.db import models
from setup.models import Asignatura, Profesor, Alumno


class Trabajo(models.Model):
    concepto = models.CharField(max_length=100)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    online = models.BooleanField(default=False)
    fechaEntrega = models.DateTimeField()

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"

    def __str__(self):
        return "{} - {}".format(self.concepto, self.asignatura)


class NotaTrabajo(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    notaNumerica = models.DecimalField(max_digits=2, decimal_places=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "NotaTrabajo"
        verbose_name_plural = "NotasTrabajos"

    def __str__(self):
        return self.notaNumerica


class EntregaTrabajoOnline(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fechaEntrega = models.DateTimeField()
    comentario = models.TextField(blank=True, null=True)
    nota = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "EntregaTrabajoOnline"
        verbose_name_plural = "EntregaTrabajoOnline"

    def __str__(self):
        return "{} / {} / {}".format(
            self.trabajo,
            self.alumno,
            self.nota
        )


class AdjuntoTrabajo(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    nombreArchivo = models.CharField(max_length=100)
    file = models.FileField(upload_to="static/documents")

    class Meta:
        verbose_name = "AdjuntoTrabajo"
        verbose_name_plural = "AdjuntoTrabajos"

    def __str__(self):
        return "{} - {}".format(self.nombreArchivo, self.trabajo)


class DocumentoEntrega(models.Model):
    entrega = models.ForeignKey(EntregaTrabajoOnline, on_delete=models.CASCADE)
    nombreArchivo = models.CharField(max_length=100)
    file = models.FileField(upload_to="static/documents")

    class Meta:
        verbose_name = "DocumentoEntrega"
        verbose_name_plural = "DocumentosEntrega"

    def __str__(self):
        return self.nombreArchivo
