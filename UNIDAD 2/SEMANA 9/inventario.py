# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        # Lista para almacenar los objetos de tipo Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Verificamos si el ID ya existe para asegurar unicidad
        if any(p.id == producto.id for p in self.productos):
            print(f"\n[Error]: El ID {producto.id} ya pertenece a otro producto.")
            return False
        self.productos.append(producto)
        print("\n[Éxito]: Producto añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                print(f"\n[Éxito]: Producto con ID {id_producto} eliminado.")
                return True
        print("\n[Error]: No se encontró un producto con ese ID.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                print("\n[Éxito]: Producto actualizado.")
                return True
        print("\n[Error]: ID no encontrado.")
        return False

    def buscar_por_nombre(self, nombre_buscado):
        # Busca coincidencias parciales (ej: "man" encuentra "manzana")
        resultados = [p for p in self.productos if nombre_buscado.lower() in p.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\n" + "="*55)
            print(f"{'LISTADO DE PRODUCTOS':^55}")
            print("="*55)
            for p in self.productos:
                print(p)
            print("="*55)