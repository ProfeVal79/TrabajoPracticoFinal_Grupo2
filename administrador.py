from usuario import Usuario
from decoradores import loggear_accion

class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, dni, email, contrasenia, nivelPermisos):
        super().__init__(id, nombre, apellido, dni, email, contrasenia)
        self.nivelPermisos = nivelPermisos

    @loggear_accion
    def gestionar(self):
        return f"Administrador {self.nombre} gestiona materiales."
