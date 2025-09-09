# ============================================
# Sistema de Gestión de Biblioteca Digital
# ============================================

from typing import Dict, List, Set, Tuple, Optional


class Libro:
    """
    Representa un libro.
    - Usa una tupla inmutable (titulo, autor) porque no cambian una vez creado.
    - Mantiene categoría (string) e ISBN (string) como atributos editables si fuese necesario.
    """
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        self._info: Tuple[str, str] = (titulo, autor)  # (titulo, autor) inmutable por diseño
        self.categoria: str = categoria
        self.isbn: str = isbn

    # Accesores de la tupla inmutable
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
    - id_usuario es único (controlado por la Biblioteca usando un conjunto).
    - libros_prestados: lista de ISBNs actualmente prestados al usuario (List[str]).
      Se usan ISBNs para enlazar fácilmente con el catálogo (diccionario).
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
    - libros: Dict[ISBN, Libro] para búsquedas eficientes por ISBN.
    - usuarios: Dict[id_usuario, Usuario] para acceder a los usuarios.
    - ids_usuarios: Set[str] para garantizar unicidad de IDs.
    - prestamos: Dict[ISBN, id_usuario] para saber si un libro está prestado y a quién.
      Un libro está disponible si su ISBN NO aparece en 'prestamos'.
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
        """Añade un libro si el ISBN no existe en el catálogo."""
        if libro.isbn in self.libros:
            print("No se añadió el libro: ya existe un libro con ese ISBN.")
            return
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro.titulo} ({libro.isbn})")

    def quitar_libro(self, isbn: str) -> None:
        """Quita un libro si existe y no está prestado."""
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
        """Registra usuario si el ID es único."""
        if usuario.id_usuario in self.ids_usuarios:
            print("No se registró: el ID de usuario ya existe.")
            return
        self.ids_usuarios.add(usuario.id_usuario)
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Usuario registrado: {usuario.nombre} (ID: {usuario.id_usuario})")

    def dar_baja_usuario(self, id_usuario: str) -> None:
        """Da de baja a un usuario si existe y no tiene libros prestados."""
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
    # Préstamo y devolución
    # -----------------------------
    def prestar_libro(self, isbn: str, id_usuario: str) -> None:
        """Presta un libro a un usuario si el libro existe, el usuario existe y el libro está disponible."""
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
        """Devuelve un libro si efectivamente estaba prestado a ese usuario."""
        if isbn not in self.prestamos:
            print("El libro no está registrado como prestado.")
            return
        if self.prestamos[isbn] != id_usuario:
            print("El libro no está prestado a ese usuario.")
            return

        # Remover del mapa de préstamos y de la lista del usuario
        self.prestamos.pop(isbn)
        usuario = self.usuarios[id_usuario]
        try:
            usuario.libros_prestados.remove(isbn)
        except ValueError:
            # En un caso ideal no debería pasar, pero lo manejamos de forma segura.
            pass
        print(f"Devolución registrada: '{self.libros[isbn].titulo}' devuelto por {usuario.nombre}")

    # -----------------------------
    # Búsquedas
    # -----------------------------
    def buscar_por_titulo(self, texto: str) -> List[Libro]:
        """Búsqueda por coincidencia parcial de título (insensible a mayúsculas)."""
        t = texto.lower()
        return [libro for libro in self.libros.values() if t in libro.titulo.lower()]

    def buscar_por_autor(self, texto: str) -> List[Libro]:
        """Búsqueda por coincidencia parcial de autor (insensible a mayúsculas)."""
        t = texto.lower()
        return [libro for libro in self.libros.values() if t in libro.autor.lower()]

    def buscar_por_categoria(self, categoria: str) -> List[Libro]:
        """Búsqueda exacta de categoría (puedes adaptar a coincidencia parcial si prefieres)."""
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]

    # -----------------------------
    # Listado de préstamos por usuario
    # -----------------------------
    def listar_prestados_usuario(self, id_usuario: str) -> List[Libro]:
        """Devuelve la lista de libros prestados a un usuario (objetos Libro)."""
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
        """Imprime libros en formato de tabla simple."""
        if not libros:
            print("No hay libros para mostrar.")
            return
        print(f"{'ISBN':<15}{'Título':<30}{'Autor':<25}{'Categoría':<15}")
        print("-" * 85)
        for l in libros:
            print(f"{l.isbn:<15}{l.titulo:<30}{l.autor:<25}{l.categoria:<15}")

# ============================================
# Pruebas del sistema (uso de las clases)
# ============================================
if __name__ == "__main__":
    bib = Biblioteca()

    # 1) Registrar usuarios
    u1 = Usuario("Ana", "U001")
    u2 = Usuario("Luis", "U002")
    bib.registrar_usuario(u1)
    bib.registrar_usuario(u2)

    # Intento con ID duplicado
    bib.registrar_usuario(Usuario("María", "U001"))

    # 2) Añadir libros
    l1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "ISBN-001")
    l2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", "ISBN-002")
    l3 = Libro("Clean Code", "Robert C. Martin", "Programación", "ISBN-003")
    bib.añadir_libro(l1)
    bib.añadir_libro(l2)
    bib.añadir_libro(l3)
    # Intento con ISBN duplicado
    bib.añadir_libro(Libro("Otro título", "Otro autor", "Otra", "ISBN-003"))

    print("\nCatálogo actual:")
    Biblioteca.imprimir_libros(list(bib.libros.values()))

    # 3) Búsquedas
    print("\nBuscar por autor='gabriel':")
    Biblioteca.imprimir_libros(bib.buscar_por_autor("gabriel"))

    print("\nBuscar por título='clean':")
    Biblioteca.imprimir_libros(bib.buscar_por_titulo("clean"))

    print("\nBuscar por categoría='novela':")
    Biblioteca.imprimir_libros(bib.buscar_por_categoria("novela"))

    # 4) Préstamos y devoluciones
    print("\nPréstamos:")
    bib.prestar_libro("ISBN-001", "U001")  # Ana toma "Cien años de soledad"
    bib.prestar_libro("ISBN-003", "U001")  # Ana toma "Clean Code"
    bib.prestar_libro("ISBN-001", "U002")  # Libro ya prestado

    print("\nLibros prestados a Ana:")
    Biblioteca.imprimir_libros(bib.listar_prestados_usuario("U001"))

    print("\nDevoluciones:")
    bib.devolver_libro("ISBN-001", "U001")
    bib.devolver_libro("ISBN-002", "U001")  # No lo tenía Ana

    print("\nLibros prestados a Ana (tras devoluciones):")
    Biblioteca.imprimir_libros(bib.listar_prestados_usuario("U001"))

    # 5) Bajas y quitas
    print("\nDar de baja a Luis (sin préstamos):")
    bib.dar_baja_usuario("U002")

    print("\nIntento de quitar un libro prestado (Clean Code aún en préstamo):")
    bib.quitar_libro("ISBN-003")

    print("\nDevolver 'Clean Code' y eliminarlo:")
    bib.devolver_libro("ISBN-003", "U001")
    bib.quitar_libro("ISBN-003")

    print("\nCatálogo final:")
    Biblioteca.imprimir_libros(list(bib.libros.values()))
