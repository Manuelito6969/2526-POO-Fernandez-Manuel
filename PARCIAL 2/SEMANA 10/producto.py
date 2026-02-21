class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @property
    def cantidad(self): return self._cantidad
    @property
    def precio(self): return self._precio

    # Setters para los valores que pueden cambiar
    @cantidad.setter
    def cantidad(self, valor): self._cantidad = valor
    @precio.setter
    def precio(self, valor): self._precio = valor

    def to_dict(self):
        """Convierte el objeto a diccionario para guardarlo en JSON."""
        return {
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre:<15} | Cantidad: {self._cantidad:<5} | Precio: ${self._precio:.2f}"