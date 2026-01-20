"""
Programa: Constructores y Destructores en Python
Descripción: Sistema simple de gestión de biblioteca
"""


class Libro:
    """
    Clase que representa un libro en una biblioteca.
    Demuestra el uso de constructores y destructores.
    """

    # Variable de clase: cuenta cuántos libros existen
    total_libros = 0

    def __init__(self, titulo, autor, paginas=100):
        """
        CONSTRUCTOR: Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos del libro.

        Parámetros:
        - titulo: nombre del libro
        - autor: autor del libro
        - paginas: número de páginas (valor por defecto: 100)
        """
        # Atributos de instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prestado = False

        # Incrementar contador
        Libro.total_libros += 1

        print(f" [CONSTRUCTOR] Libro creado: '{self.titulo}'")
        print(f"   Autor: {self.autor} | Páginas: {self.paginas}")
        print(f"   Total de libros en sistema: {Libro.total_libros}\n")

    def prestar(self):
        """Marca el libro como prestado"""
        if not self.prestado:
            self.prestado = True
            print(f" Libro '{self.titulo}' prestado\n")
        else:
            print(f" El libro '{self.titulo}' ya está prestado\n")

    def devolver(self):
        """Marca el libro como devuelto"""
        if self.prestado:
            self.prestado = False
            print(f" Libro '{self.titulo}' devuelto\n")
        else:
            print(f"ℹ El libro '{self.titulo}' no estaba prestado\n")

    def __del__(self):
        """
        DESTRUCTOR: Se ejecuta automáticamente cuando el objeto se elimina.
        Útil para liberar recursos (cerrar archivos, conexiones, etc.)
        """
        Libro.total_libros -= 1
        print(f" [DESTRUCTOR] Libro '{self.titulo}' eliminado del sistema")
        print(f"   Libros restantes: {Libro.total_libros}\n")


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    """

    def __init__(self, nombre, edad):
        """
        CONSTRUCTOR: Inicializa los datos del usuario.
        """
        self.nombre = nombre
        self.edad = edad
        self.libros_prestados = []

        print(f" [CONSTRUCTOR] Usuario registrado: {self.nombre}")
        print(f"   Edad: {self.edad} años\n")

    def tomar_libro(self, libro):
        """El usuario toma un libro prestado"""
        self.libros_prestados.append(libro.titulo)
        libro.prestar()

    def devolver_libro(self, libro):
        """El usuario devuelve un libro"""
        if libro.titulo in self.libros_prestados:
            self.libros_prestados.remove(libro.titulo)
            libro.devolver()

    def __del__(self):
        """
        DESTRUCTOR: Limpia los datos del usuario.
        """
        print(f" [DESTRUCTOR] Usuario '{self.nombre}' eliminado del sistema\n")


# ==================== PROGRAMA PRINCIPAL ====================

def main():
    print("="*50)
    print("  SISTEMA DE BIBLIOTECA - DEMO DE CONSTRUCTORES")
    print("="*50)
    print()

    # Los CONSTRUCTORES se ejecutan aquí al crear los objetos
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 432)
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", 863)
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")  # usa valor por defecto

    usuario1 = Usuario("Ana García", 25)
    usuario2 = Usuario("Carlos López", 30)

    print("-" * 50)
    print("  OPERACIONES DE PRÉSTAMO")
    print("-" * 50)
    print()

    # Realizar operaciones
    usuario1.tomar_libro(libro1)
    usuario2.tomar_libro(libro2)
    usuario1.devolver_libro(libro1)

    print("-" * 50)
    print("  ELIMINACIÓN DE OBJETOS")
    print("-" * 50)
    print()

    # El DESTRUCTOR se ejecuta al eliminar objetos con 'del'
    print("Eliminando libro2...")
    del libro2

    print("Eliminando usuario2...")
    del usuario2

    print("-" * 50)
    print("  FIN DEL PROGRAMA")
    print("-" * 50)
    print()
    print("Los objetos restantes se destruirán automáticamente")
    print("al finalizar el programa...\n")

    # Al terminar main(), todos los objetos restantes se destruyen
    # y sus DESTRUCTORES se ejecutan automáticamente


if __name__ == "__main__":
    main()

    print("\n Programa finalizado")