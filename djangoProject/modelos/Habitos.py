# Objecto habitos con los parametros Habitos	Acción	Media Actual	Unidad de registro	Unidad de media	Unidad de
# registro	Unidad de revision	Proceso


class Habitos():
    def __str__(self):
        return self.habitos

    # Contructor de la clase
    def __init__(self, idHabito, habito, accion, mediaActual, unidadRegistro, unidadMedia, unidadRevision, proceso):
        self.idHabito = idHabito
        self.habito = habito
        self.accion = accion
        self.mediaActual = mediaActual
        self.unidadRegistro = unidadRegistro
        self.unidadMedia = unidadMedia
        self.unidadRevision = unidadRevision
        self.proceso = proceso
