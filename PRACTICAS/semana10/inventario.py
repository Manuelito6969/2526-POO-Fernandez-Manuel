from typing import List, Optional
from producto import Producto
from archivo import GestionInventario

class Inventario:
    """
    Lógica de negocio simple. Delegamos la carga/guardado en ArchivoInventario.
    """
    def __init__(self, ruta_archivo: str):
        self.storage = GestionInventario(ruta_archivo)
        self.productos: List[Producto] = self.storage.cargar()

    # Operaciones
    def anadir_producto(self, p: Producto) -> None:
        if any(x.get_id() == p.get_id() for x in self.productos):
            print("El ID ya existe. No se añadió el producto.")
            return
        self.productos.append(p)
        if self.storage.guardar(self.productos):
            print("Producto añadido y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. El producto permanece en memoria.")

    def eliminar_producto(self, id_producto: str) -> None:
        original = len(self.productos)
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        if len(self.productos) == original:
            print("Producto no encontrado.")
            return
        if self.storage.guardar(self.productos):
            print("Producto eliminado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    def actualizar_producto(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None) -> None:
        encontrado = False
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
            return
        if self.storage.guardar(self.productos):
            print("Producto actualizado y guardado en archivo.")
        else:
            print("No se pudo guardar en archivo. Cambios solo en memoria.")

    # Consultas: devuelven listas; no imprimen
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def obtener_todos(self) -> List[Producto]:
        return list(self.productos)

    def recargar(self) -> None:
        self.productos = self.storage.cargar()
        print("Inventario recargado desde archivo.")

    # Presentación: imprime una tabla a partir de una lista
    def imprimir_tabla(self, productos: List[Producto]) -> None:
        if not productos:
            print("No hay productos para mostrar.")
            return
        print(f"{'ID':<8}{'Nombre':<20}{'Cantidad':<12}{'Precio':<10}")
        print("-" * 50)
        for p in productos:
            print(f"{p.get_id():<8}{p.get_nombre():<20}{p.get_cantidad():<12}{p.get_precio():<10.2f}")
