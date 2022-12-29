import json


class Usuario:

    def __init__(self, id,nombre, contrasenia, administrador):
        self.id = id
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.administrador = administrador

    def __str__(self):
        return "id:" + self.id + "nombre: " + self.nombre + " contrasenia: " + self.contrasenia + " administrador: " + str(self.administrador)

#metodo to_json
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#metodo to_dict
    def to_dict(self):
        return json.loads(self.to_json())
