from metaclase import MetaEntidad
from decoradores import loggear_accion

class BibliotecaDigital(metaclass=MetaEntidad):
    _instancia = None

    def __new__(cls, id, nombre, url, email):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, id, nombre, url, email):
        self.id = id
        self.nombre = nombre
        self.url = url
        self.email = email
        self.materiales = []   # agregación: lista de materiales
        self.usuarios = []

    @loggear_accion
    def agregar_material(self, material):
        self.materiales.append(material)

    @loggear_accion
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
