from metaclase import MetaEntidad

class MaterialDigital(metaclass=MetaEntidad):
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def obtener_estado(self):
        return "Disponible"

class Libro(MaterialDigital):
    def __init__(self, id, titulo, autor, ISBN, anio, paginas):
        super().__init__(id, titulo, autor)
        self.ISBN = ISBN
        self.anio = anio
        self.paginas = paginas

