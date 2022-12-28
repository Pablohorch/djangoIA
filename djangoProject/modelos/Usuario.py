import json


class Usuario:

    def __init__(self, nombre, contrasenia, administrador):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.administrador = administrador

    def __str__(self):
        return "nombre: " + self.nombre + " contrasenia: " + self.contrasenia + " administrador: " + str(self.administrador)

#metodo to_json
    def to_json(self):
        return json.dumps

#metodo to_dict
    def to_dict(self):
        return json.loads(self.to_json())
