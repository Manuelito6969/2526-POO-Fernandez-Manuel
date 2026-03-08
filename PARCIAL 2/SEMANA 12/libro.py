class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Validaciones básicas: todos deben ser cadenas no vacías
        if not (isinstance(titulo, str) and titulo.strip()):
            raise ValueError("titulo debe ser una cadena no vacía")
        if not (isinstance(autor, str) and autor.strip()):
            raise ValueError("autor debe ser una cadena no vacía")
        if not (isinstance(categoria, str) and categoria.strip()):
            raise ValueError("categoria debe ser una cadena no vacía")
        if isbn is None:
            raise ValueError("isbn no puede ser None")

        # Normalizamos y almacenamos
        self.datos_base = (titulo.strip(), autor.strip())
        self.categoria = categoria.strip()
        self.isbn = str(isbn).strip()

    @property
    def titulo(self): return self.datos_base[0]

    @property
    def autor(self): return self.datos_base[1]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} [ISBN: {self.isbn}] - Categoría: {self.categoria}"

    def __repr__(self):
        return f"Libro(titulo={self.titulo!r}, autor={self.autor!r}, isbn={self.isbn!r})"
