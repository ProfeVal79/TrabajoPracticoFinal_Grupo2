from biblioteca_digital import BibliotecaDigital
from material import Libro
from usuario_final import UsuarioFinal
from administrador import Administrador
from prestamo import Prestamo
from datetime import datetime, timedelta

if __name__ == "__main__":
    # Singleton: crear la biblioteca
    biblioteca = BibliotecaDigital(1, "MiBiblioteca", "www.biblio.com", "info@biblio.com")

    # Crear materiales
    libro1 = Libro(101, "Python Avanzado", "Guido", "12345", 2020, 350)
    libro2 = Libro(102, "Algoritmos", "Knuth", "67890", 1998, 1200)

    biblioteca.agregar_material(libro1)
    biblioteca.agregar_material(libro2)

    # Crear usuarios
    usuario1 = UsuarioFinal(201, "Valeria", "Igarzabal", "12345678", "valeria@mail.com", "clave123")
    admin1 = Administrador(301, "Carlos", "Perez", "87654321", "carlos@mail.com", "adminpass", "Alto")

    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(admin1)

    # Polimorfismo: ambos redefinen gestionar()
    print(usuario1.gestionar())
    print(admin1.gestionar())

    # Crear préstamos (composición)
    fecha_entrega = datetime.now()
    fecha_devolucion = fecha_entrega + timedelta(days=7)
    prestamo1 = Prestamo(401, usuario1, libro1, fecha_entrega, fecha_devolucion)

    usuario1.agregar_prestamo(prestamo1)

    # Métodos de Prestamo
    print(f"Días de retraso: {prestamo1.calcular_dias_retraso()}")

    # Historial de préstamos del usuario
    print(usuario1.mostrar_historial())

    # Métodos de BibliotecaDigital
    print("Materiales en la biblioteca:")
    for m in biblioteca.materiales:
        print(f"- {m.titulo} ({m.autor})")

    print("Usuarios en la biblioteca:")
    for u in biblioteca.usuarios:
        print(f"- {u.nombre} {u.apellido}")

    print(f"bienvenidos a la biblioteca: {biblioteca.nombre}")

    biblioteca2 = BibliotecaDigital(2, "Biblioteca Central", "www.biblio.com", "info@biblio.com" )
    print(f"bienvenidos a la biblioteca: {biblioteca2.nombre}")
    print(biblioteca.nombre, biblioteca2.nombre)
    print(biblioteca is biblioteca2)

    print(biblioteca.id)

    biblioteca2.registrar_usuario(usuario1)
    usuario1.solicitar_baja()
    admin1.gestionar_baja(usuario1)



