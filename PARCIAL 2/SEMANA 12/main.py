from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def probar_biblioteca():
    mi_biblioteca = Biblioteca()

    # 1. Crear Libros
    l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-01")
    l2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "978-02")

    # 2. Añadir Libros
    ok = mi_biblioteca.añadir_libro(l1)
    print("Añadir l1:", "OK" if ok else "Fallo")
    ok = mi_biblioteca.añadir_libro(l2)
    print("Añadir l2:", "OK" if ok else "Fallo")

    # Intentar añadir duplicado
    ok = mi_biblioteca.añadir_libro(l1)
    print("Añadir l1 (duplicado):", "OK" if ok else "Fallo esperado")

    # 3. Registrar Usuarios
    user1 = Usuario("Manuel Fernandez", "ID100")
    ok = mi_biblioteca.registrar_usuario(user1)
    print("Registrar user1:", "OK" if ok else "Fallo")

    # Intentar registrar de nuevo el mismo ID
    ok = mi_biblioteca.registrar_usuario(user1)
    print("Registrar user1 (duplicado):", "OK" if ok else "Fallo esperado")

    # 4. Prestar Libro
    ok = mi_biblioteca.prestar_libro("ID100", "978-01")
    print("Prestar 978-01 a ID100:", "OK" if ok else "Fallo")

    # Intentar prestar un libro no disponible
    ok = mi_biblioteca.prestar_libro("ID100", "978-01")
    print("Prestar 978-01 otra vez:", "OK" if ok else "Fallo esperado")

    # 5. Listar prestados
    print(user1)

    # 6. Devolver Libro
    ok = mi_biblioteca.devolver_libro("ID100", "978-01")
    print("Devolver 978-01 por ID100:", "OK" if ok else "Fallo")

    # Intentar devolver de nuevo
    ok = mi_biblioteca.devolver_libro("ID100", "978-01")
    print("Devolver 978-01 otra vez:", "OK" if ok else "Fallo esperado")


if __name__ == "__main__":
    probar_biblioteca()