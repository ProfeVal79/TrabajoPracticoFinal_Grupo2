from metaclase import MetaEntidad

class Prestamo(metaclass=MetaEntidad):
    def __init__(self, id, usuario, libro, fecha_entrega, fecha_devolucion):
        self.id = id
        self.usuario = usuario
        self.libro = libro  # composición: el préstamo contiene el libro
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion

    def calcular_dias_retraso(self):
        return (self.fecha_devolucion - self.fecha_entrega).days


    


    