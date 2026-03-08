class Usuario:
    def __init__(self, nombre, id_usuario):
        if not (isinstance(nombre, str) and nombre.strip()):
            raise ValueError("nombre debe ser una cadena no vacía")
        if not (isinstance(id_usuario, str) and id_usuario.strip()):
            raise ValueError("id_usuario debe ser una cadena no vacía")

        self.nombre = nombre.strip()
        self.id_usuario = id_usuario.strip()
        # Lista de libros actualmente prestados
        self.libros_prestados = []

    def agregar_prestado(self, libro):
        # No permitimos duplicados por ISBN
        if any(l.isbn == libro.isbn for l in self.libros_prestados):
            return False
        self.libros_prestados.append(libro)
        return True

    def quitar_prestado(self, isbn):
        for libro in list(self.libros_prestados):
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        titulos = [l.titulo for l in self.libros_prestados]
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros: {titulos}"
