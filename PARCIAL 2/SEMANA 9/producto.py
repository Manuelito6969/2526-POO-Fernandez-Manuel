# producto.py

class Producto:
    """
    Clase que representa un producto individual en la tienda.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados para seguir el principio de encapsulamiento
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters (Usando decoradores property)
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"ID: {self._id:03d} | Nombre: {self._nombre:<15} | Stock: {self._cantidad:4d} | Precio: ${self._precio:>7.2f}"


