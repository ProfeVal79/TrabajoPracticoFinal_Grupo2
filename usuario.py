from metaclase import MetaEntidad

class Usuario(metaclass=MetaEntidad):
    def __init__(self, id, nombre, apellido, dni, email, contrasenia):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.contrasenia = contrasenia

    def gestionar(self):
        raise NotImplementedError("Debe implementarse en subclases")

                
        
            