class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters (para obtener valores)
    @property
    def id(self): return self._id

    @property
    def nombre(self): return self._nombre

    @property
    def cantidad(self): return self._cantidad

    @property
    def precio(self): return self._precio

    # Setters (para modificar valores)
    @nombre.setter
    def nombre(self, valor): self._nombre = valor

    @cantidad.setter
    def cantidad(self, valor): self._cantidad = valor

    @precio.setter
    def precio(self, valor): self._precio = valor

    def __str__(self):
        """Devuelve una cadena amigable al imprimir el objeto."""
        return f"ID: {self._id} | Nombre: {self._nombre:<15} | Cantidad: {self._cantidad:<5} | Precio: ${self._precio:.2f}"