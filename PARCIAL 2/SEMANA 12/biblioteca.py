class Biblioteca:
    def __init__(self):
        self.libros = {}       # {isbn: objeto_Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos
        self.registro_usuarios = {} # {id_usuario: objeto_Usuario}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro.titulo}")
        else:
            print("Error: El ISBN ya existe.")
            return False

    # alias sin acento
    anadir_libro = añadir_libro

    def registrar_usuario(self, usuario):
        if not hasattr(usuario, 'id_usuario') or not usuario.id_usuario:
            print("Error: usuario inválido (falta id).")
            return False
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
            return True
        else:
            print("Error: El ID de usuario ya está en uso.")
            return False

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Error: Usuario no registrado.")
            return False
        if isbn not in self.libros:
            print("Error: ISBN no disponible en la biblioteca.")
            return False

        usuario = self.registro_usuarios[id_usuario]
        libro = self.libros[isbn]
        # Intentamos agregar al usuario; si falla no removemos del catálogo
        if usuario.agregar_prestado(libro):
            self.libros.pop(isbn)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            return True
        else:
            print(f"Error: El usuario ya tiene prestado el libro con ISBN {isbn}.")
            return False

    prestar = prestar_libro

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Error: Usuario no registrado.")
            return False
        usuario = self.registro_usuarios[id_usuario]
        libro = usuario.quitar_prestado(isbn)
        if libro:
            self.libros[isbn] = libro # Vuelve a estar disponible
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            return True
        else:
            print("Error: El usuario no tiene prestado ese libro.")
            return False

    devolver = devolver_libro

    def buscar_libro(self, criterio):
        # Si criterio vacío, devolver todos los libros disponibles
        if not criterio:
            return list(self.libros.values())

        c = criterio.lower()
        encontrados = [l for l in self.libros.values() if
                       (getattr(l, 'titulo', '').lower().find(c) != -1) or
                       (getattr(l, 'autor', '').lower().find(c) != -1) or
                       (getattr(l, 'categoria', '').lower().find(c) != -1)]
        return encontrados