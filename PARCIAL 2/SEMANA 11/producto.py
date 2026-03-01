class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Validaciones básicas
        try:
            self._id = int(id_producto)
        except (TypeError, ValueError):
            raise ValueError("El ID debe ser un número entero válido.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")

        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad_int < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        try:
            precio_f = float(precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número (float).")
        if precio_f < 0:
            raise ValueError("El precio no puede ser negativo.")

        self._id = self._id
        self._nombre = nombre.strip()
        self._cantidad = cantidad_int
        self._precio = precio_f

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        try:
            v = int(valor)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero.")
        if v < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = v

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            v = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número.")
        if v < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = v

    def to_dict(self):
        """Para serialización en JSON."""
        return {"nombre": self._nombre, "cantidad": self._cantidad, "precio": self._precio}

    @classmethod
    def from_dict(cls, id_producto, data):
        """Crear Producto desde un diccionario (por ejemplo, cargado del JSON)."""
        if not isinstance(data, dict):
            raise ValueError("Los datos deben ser un diccionario.")
        nombre = data.get('nombre')
        cantidad = data.get('cantidad')
        precio = data.get('precio')
        return cls(id_producto, nombre, cantidad, precio)

    def __str__(self):
        return f"ID: {self._id} | {self._nombre} | Cantidad: {self._cantidad} | Precio: {self._precio:.2f}"
