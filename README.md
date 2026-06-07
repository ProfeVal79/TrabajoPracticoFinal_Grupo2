# 📚 Biblioteca Digital en Python

## 🔹 Descripción general
Este proyecto implementa un sistema de **Biblioteca Digital** en Python, modelando usuarios, materiales digitales, préstamos y la propia biblioteca.  
Se aplican conceptos avanzados de programación orientada a objetos y patrones de diseño, integrando:

- Herencia
- Polimorfismo
- Agregación
- Composición
- Decoradores
- Metaclases
- Patrón Singleton

---

## 🔹 Funcionalidades aplicadas
- **Herencia:** `UsuarioFinal` y `Administrador` heredan de `Usuario`.  
- **Polimorfismo:** el método `gestionar()` se redefine en cada subclase.  
- **Agregación:** `BibliotecaDigital` mantiene listas de materiales y usuarios.  
- **Composición:** `Prestamo` contiene directamente un `Libro`.  
- **Decorador propio:** `@loggear_accion` registra acciones en consola.  
- **Metaclase (`MetaEntidad`):** asegura que todas las clases tengan un atributo `id`.  
- **Patrón Singleton:** `BibliotecaDigital` solo puede tener una instancia.  

---

## 🔹 Estructura del proyecto
biblioteca/
│
├── metaclase.py
├── decoradores.py
├── material.py
├── prestamo.py
├── usuario.py
├── usuario_final.py
├── administrador.py
├── biblioteca_digital.py
└── main.py

---

## 🔹 Clases principales

### `MetaEntidad` (metaclase)
- Deriva de `type`.  
- Garantiza que todas las clases tengan un atributo `id`.  
- Se usa como metaclase en `Usuario`, `MaterialDigital`, `Prestamo` y `BibliotecaDigital`.

---

### `MaterialDigital`
- Clase base para materiales de la biblioteca.  
- Atributos: `id`, `titulo`, `autor`.  
- Método: `obtener_estado()` → devuelve disponibilidad.  

#### `Libro` (subclase)
- Hereda de `MaterialDigital`.  
- Atributos adicionales: `ISBN`, `anio`, `paginas`.  

---

### `Prestamo`
- Representa un préstamo de un libro.  
- Atributos: `id`, `usuario`, `libro`, `fecha_entrega`, `fecha_devolucion`.  
- Métodos:  
  - `calcular_dias_retraso()` → calcula días de retraso.  

---

### `Usuario`
- Clase abstracta base para usuarios.  
- Atributos: `id`, `nombre`, `apellido`, `dni`, `email`, `contrasenia`.  
- Método: `gestionar()` → debe redefinirse en subclases.  

#### `UsuarioFinal`
- Hereda de `Usuario`.  
- Atributos: `historial_prestamo`.  
- Métodos:  
  - `gestionar()` → solicita préstamo.  
  - `agregar_prestamo()` → guarda préstamos en historial.  
  - `mostrar_historial()` → lista préstamos realizados.  

#### `Administrador`
- Hereda de `Usuario`.  
- Atributos: `nivelPermisos`.  
- Métodos:  
  - `gestionar()` → gestiona materiales y usuarios.  

---

### `BibliotecaDigital` (Singleton)
- Clase principal del sistema.  
- Atributos: `id`, `nombre`, `url`, `email`, `materiales`, `usuarios`.  
- Métodos:  
  - `agregar_material()` → añade materiales.  
  - `agregar_usuario()` → añade usuarios.  

---

### `Decorador: loggear_accion`
- Se aplica a métodos clave (`gestionar`, `agregar_material`, `agregar_usuario`).  
- Imprime un log en consola cada vez que se ejecuta un método decorado.

✅ Conclusión
Este sistema demuestra cómo integrar conceptos avanzados de Python en un proyecto realista:

Metaclases para imponer reglas globales.

Decoradores para logging.

Herencia y polimorfismo para jerarquías de usuarios.

Agregación y composición para relaciones entre entidades.

Singleton para garantizar una única instancia de la biblioteca.

***BibliotecaDigital*** se implementa como ***Singleton*** porque en el modelo de una biblioteca digital, debe existir una única instancia centralizada que gestione todos los materiales y usuarios.


### Justificación conceptual:

Si tuviera varias instancias de ***BibliotecaDigital***, cada una tendría su propia lista de usuarios y materiales y eso generaría inconsistencias (un mismo libro podría estar duplicado en distintas bibliotecas, o un usuario podría existir en una pero no en otra).

El patrón ***Singleton*** asegura que solo exista una biblioteca en todo el sistema, y que todas las operaciones (agregar usuarios, registrar préstamos, buscar materiales) se hagan sobre esa misma instancia.

Es como tener una base de datos única que centraliza la información.


---

## 🔹 Ejemplo de ejecución
```bash
python main.py
[LOG] Ejecutando agregar_material
[LOG] Ejecutando agregar_usuario
[LOG] Ejecutando agregar_usuario
[LOG] Ejecutando gestionar
UsuarioFinal Valeria solicita préstamo.
[LOG] Ejecutando gestionar
Administrador Carlos gestiona materiales.
Libro: Python Avanzado, Entrega: 2026-06-07 01:24:00, Devolución: 2026-06-14 01:24:00
Materiales en la biblioteca:
- Python Avanzado (Guido)
- Algoritmos (Knuth)
Usuarios en la biblioteca:
- Valeria Igarzabal
- Carlos Perez








