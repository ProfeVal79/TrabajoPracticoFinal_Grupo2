class MetaEntidad(type):
    def __new__(cls, nombre, bases, diccionario):
        if 'id' not in diccionario:
            diccionario['id'] = None
        return super().__new__(cls, nombre, bases, diccionario)
