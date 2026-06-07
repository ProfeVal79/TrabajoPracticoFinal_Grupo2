def loggear_accion(funcion):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando {funcion.__name__}")
        return funcion(*args, **kwargs)
    return wrapper
