from usuario import Usuario
from decoradores import loggear_accion
from biblioteca_digital import BibliotecaDigital

class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, dni, email, contrasenia, nivelPermisos):
        super().__init__(id, nombre, apellido, dni, email, contrasenia)
        self.nivelPermisos = nivelPermisos

    def gestionar_baja(self, usuario):
        if usuario.solicitud_baja:
            print(f"El administrador dio de baja al usuario {usuario.nombre} {usuario.apellido}.")
            # Aquí podrías eliminarlo de la lista de usuarios de la BibliotecaDigital
            BibliotecaDigital._instancia.eliminar_usuario(usuario)
        else:
            print(f"El usuario {usuario.nombre} {usuario.apellido} no solicitó la baja.")

    @loggear_accion
    def gestionar(self):
        return f"Administrador {self.nombre} gestiona materiales."
