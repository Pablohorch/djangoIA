# Objecto habitos con los parametros Habitos	Acción	Media Actual	Unidad de registro	Unidad de media	Unidad de
# registro	Unidad de revision	Proceso
from django.forms import models


class Habitos(models.Model):
    def __str__(self):
        return self.habitos

    # Contructor de la clase
    def __init__(self, habitos, accion, mediaActual, unidadRegistro, unidadMedia, unidadRevision, proceso):
        self.habitos = habitos
        self.accion = accion
        self.MediaActual = mediaActual
        self.unidadRegistro = unidadRegistro
        self.unidadMedia = unidadMedia
        self.unidadRevision = unidadRevision
        self.proceso = proceso
