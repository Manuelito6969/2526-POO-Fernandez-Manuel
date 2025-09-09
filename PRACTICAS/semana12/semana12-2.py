# ============================================
# Sistema de Gestión de Biblioteca Digital
# Con menú de consola
# ============================================

from typing import Dict, List, Set, Tuple


class Libro:
    """
    Representa un libro.
    - Usa una tupla inmutable (titulo, autor) porque no cambian una vez creado.
    - Mantiene categoría (string) e ISBN (string).
    """
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._info: Tuple[str, str] = (titulo, autor)  # inmutable por diseño
        self.categoria: str = categoria
        self.isbn: str = isbn

    @property
    def titulo(self) -> str:
        return self._info[0]

    @property
    def autor(self) -> str:
        return self._info[1]

    def __repr__(self) -> str:
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', cat='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    """
    Representa a un usuario de la biblioteca.
    - id_usuario es único (controlado por Biblioteca con un conjunto).
    - libros_prestados: lista de ISBNs actualmente prestados.
    """
    def __init__(self, nombre: str, id_usuario: str):
        self.nombre: str = nombre
        self.id_usuario: str = id_usuario
        self.libros_prestados: List[str] = []  # lista de ISBNs

    def __repr__(self) -> str:
        return f"Usuario(nombre='{self.nombre}', id='{self.id_usuario}', prestados={len(self.libros_prestados)})"


class Biblioteca:
    """
    Gestiona libros, usuarios y préstamos.
    - libros: Dict[ISBN, Libro]
    - usuarios: Dict[id_usuario, Usuario]
    - ids_usuarios: Set[str] para unicidad de IDs
    - prestamos: Dict[ISBN, id_usuario]
    """
    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios: Dict[str, Usuario] = {}
        self.ids_usuarios: Set[str] = set()
        self.prestamos: Dict[str, str] = {}

    # -----------------------------
    # Gestión de libros
    # -----------------------------
    def añadir_libro(self, libro: Libro) -> None:
        if libro.isbn in self.libros:
            print("No se añadió el libro: ya existe un libro con ese ISBN.")
            return
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro.titulo} ({libro.isbn})")

    def quitar_libro(self, isbn: str) -> None:
        if isbn not in self.libros:
            print("No se encontró un libro con ese ISBN.")
            return
        if isbn in self.prestamos:
            print("No se puede quitar: el libro está prestado actualmente.")
            return
        eliminado = self.libros.pop(isbn)
        print(f"Libro eliminado: {eliminado.titulo} ({isbn})")

    # -----------------------------
    # Gestión de usuarios
    # -----------------------------
    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.id_usuario in self.ids_usuarios:
            print("No se registró: el ID de usuario ya existe.")
            return
        self.ids_usuarios.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Usuario registrado: {usuario.nombre} (ID: {usuario.id_usuario})")

    def dar_baja_usuario(self, id_usuario: str) -> None:
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print("No se puede dar de baja: el usuario tiene libros prestados.")
            return
        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario dado de baja: {id_usuario}")

    # -----------------------------
    # Préstamos
    # -----------------------------
    def prestar_libro(self, isbn: str, id_usuario: str) -> None:
        if isbn not in self.libros:
            print("No existe un libro con ese ISBN.")
            return
        if id_usuario not in self.usuarios:
            print("No existe el usuario indicado.")
            return
        if isbn in self.prestamos:
            print("El libro ya está prestado.")
            return
        self.prestamos[isbn] = id_usuario
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        print(f"Préstamo exitoso: '{self.libros[isbn].titulo}' a {self.usuarios[id_usuario].nombre}")

    def devolver_libro(self, isbn: str, id_usuario: str) -> None:
        if isbn not in self.prestamos:
            print("El libro no está registrado como prestado.")
            return
        if self.prestamos[isbn] != id_usuario:
            print("El libro no está prestado a ese usuario.")
            return
        self.prestamos.pop(isbn)
        usuario = self.usuarios[id_usuario]
        try:
            usuario.libros_prestados.remove(isbn)
        except ValueError:
            pass
        print(f"Devolución registrada: '{self.libros[isbn].titulo}' devuelto por {usuario.nombre}")

    # -----------------------------
    # Búsquedas
    # -----------------------------
    def buscar_por_titulo(self, texto: str) -> List[Libro]:
        t = texto.lower()
        return [libro for libro in self.libros.values() if t in libro.titulo.lower()]

    def buscar_por_autor(self, texto: str) -> List[Libro]:
        t = texto.lower()
        return [libro for libro in self.libros.values() if t in libro.autor.lower()]

    def buscar_por_categoria(self, categoria: str) -> List[Libro]:
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]

    # -----------------------------
    # Listado de préstamos por usuario
    # -----------------------------
    def listar_prestados_usuario(self, id_usuario: str) -> List[Libro]:
        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return []
        isbns = self.usuarios[id_usuario].libros_prestados
        return [self.libros[i] for i in isbns if i in self.libros]

    # -----------------------------
    # Utilidades de impresión
    # -----------------------------
    @staticmethod
    def imprimir_libros(libros: List[Libro]) -> None:
        if not libros:
            print("No hay libros para mostrar.")
            return
        print(f"{'ISBN':<15}{'Título':<30}{'Autor':<25}{'Categoría':<15}")
        print("-" * 85)
        for l in libros:
            print(f"{l.isbn:<15}{l.titulo:<30}{l.autor:<25}{l.categoria:<15}")

    @staticmethod
    def imprimir_usuarios(usuarios: List[Usuario]) -> None:
        if not usuarios:
            print("No hay usuarios para mostrar.")
            return
        print(f"{'ID Usuario':<12}{'Nombre':<25}{'Prestados':<10}")
        print("-" * 50)
        for u in usuarios:
            print(f"{u.id_usuario:<12}{u.nombre:<25}{len(u.libros_prestados):<10}")


# ============================================
# Menú de consola
# ============================================

def menu():
    bib = Biblioteca()

    while True:
        print("\n=== Biblioteca Digital ===")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros por título")
        print("8. Buscar libros por autor")
        print("9. Buscar libros por categoría")
        print("10. Listar libros prestados a un usuario")
        print("11. Listar todo el catálogo")
        print("12. Listar todos los usuarios")
        print("13. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            categoria = input("Categoría: ").strip()
            isbn = input("ISBN: ").strip()
            bib.añadir_libro(Libro(titulo, autor, categoria, isbn))
            input("Enter para continuar...")

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ").strip()
            bib.quitar_libro(isbn)
            input("Enter para continuar...")

        elif opcion == "3":
            nombre = input("Nombre del usuario: ").strip()
            idu = input("ID de usuario (único): ").strip()
            bib.registrar_usuario(Usuario(nombre, idu))
            input("Enter para continuar...")

        elif opcion == "4":
            idu = input("ID de usuario a dar de baja: ").strip()
            bib.dar_baja_usuario(idu)
            input("Enter para continuar...")

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ").strip()
            idu = input("ID del usuario: ").strip()
            bib.prestar_libro(isbn, idu)
            input("Enter para continuar...")

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ").strip()
            idu = input("ID del usuario: ").strip()
            bib.devolver_libro(isbn, idu)
            input("Enter para continuar...")

        elif opcion == "7":
            t = input("Texto a buscar en títulos: ").strip()
            resultados = bib.buscar_por_titulo(t)
            Biblioteca.imprimir_libros(resultados)
            input("Enter para continuar...")

        elif opcion == "8":
            a = input("Texto a buscar en autores: ").strip()
            resultados = bib.buscar_por_autor(a)
            Biblioteca.imprimir_libros(resultados)
            input("Enter para continuar...")

        elif opcion == "9":
            c = input("Categoría exacta a buscar: ").strip()
            resultados = bib.buscar_por_categoria(c)
            Biblioteca.imprimir_libros(resultados)
            input("Enter para continuar...")

        elif opcion == "10":
            idu = input("ID de usuario: ").strip()
            prestamos = bib.listar_prestados_usuario(idu)
            Biblioteca.imprimir_libros(prestamos)
            input("Enter para continuar...")

        elif opcion == "11":
            Biblioteca.imprimir_libros(list(bib.libros.values()))
            input("Enter para continuar...")

        elif opcion == "12":
            Biblioteca.imprimir_usuarios(list(bib.usuarios.values()))
            input("Enter para continuar...")

        elif opcion == "13":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")
            input("Enter para continuar...")


if __name__ == "__main__":
    menu()
