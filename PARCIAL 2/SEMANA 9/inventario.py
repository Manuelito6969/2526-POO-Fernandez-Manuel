from producto import Producto

class Inventario:
    def __init__(self):
        # Usamos una lista como estructura de datos personalizada
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto validando que el ID sea único."""
        for p in self.productos:
            if p.id == producto.id:
                print("Error: Ya existe un producto con ese ID.")
                return False
        self.productos.append(producto)
        print("Producto agregado exitosamente.")
        return True

    def eliminar_producto(self, id_buscar):
        """Elimina un producto por su ID."""
        for p in self.productos:
            if p.id == id_buscar:
                self.productos.remove(p)
                print("Producto eliminado.")
                return True
        print("Error: Producto no encontrado.")
        return False

    def actualizar_producto(self, id_buscar, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad o precio si se proporcionan."""
        for p in self.productos:
            if p.id == id_buscar:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                print("Producto actualizado.")
                return True
        print("Error: No se encontró el producto para actualizar.")

    def buscar_por_nombre(self, nombre_buscar):
        """Busca coincidencias parciales por nombre."""
        encontrados = [p for p in self.productos if nombre_buscar.lower() in p.nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        """Muestra la lista completa."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)