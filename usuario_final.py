from usuario import Usuario
from decoradores import loggear_accion

class UsuarioFinal(Usuario):
    def __init__(self, id, nombre, apellido, dni, email, contrasenia):
        super().__init__(id, nombre, apellido, dni, email, contrasenia)
        self.historial_prestamo = []
        self.solicitud_baja = False

    def solicitar_baja(self):
        self.solicitud_baja = True
        print(f"El usuario {self.nombre} {self.apellido} solicitó la baja.")

    @loggear_accion
    def gestionar(self):
        return f"UsuarioFinal {self.nombre} solicita préstamo."

    def agregar_prestamo(self, prestamo):
        self.historial_prestamo.append(prestamo)

    def mostrar_historial(self):
        if not self.historial_prestamo:
            return f"{self.nombre} no tiene préstamos registrados."
        historial = []
        for p in self.historial_prestamo:
            historial.append(
                f"Libro: {p.libro.titulo}, Entrega: {p.fecha_entrega}, Devolución: {p.fecha_devolucion}"
            )
        return "\n".join(historial)

