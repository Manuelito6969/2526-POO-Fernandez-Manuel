import json
import os
import tempfile
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: Producto}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Deserialización con manejo de excepciones."""
        self.productos = {}
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    for id_p, info in datos.items():
                        # Usar Producto.from_dict para validación
                        try:
                            p = Producto.from_dict(int(id_p), info)
                            self.productos[p.id] = p
                        except Exception as e:
                            print(f"Aviso: Producto con ID {id_p} ignorado por error: {e}")
        except json.JSONDecodeError:
            print("Error: Archivo JSON corrupto. Se ignorarán los datos y se iniciará un inventario vacío.")
        except Exception as e:
            print(f"Aviso: No se pudo cargar el archivo ({e}).")

    def guardar_en_archivo(self):
        """Serialización para almacenamiento persistente usando escritura atómica.

        Escribe en un archivo temporal y luego reemplaza el archivo destino.
        """
        try:
            datos = {str(id_p): p.to_dict() for id_p, p in self.productos.items()}
            dirpath = os.path.dirname(os.path.abspath(self.archivo)) or '.'
            # Crear archivo temporal en el mismo directorio
            fd, tmp_path = tempfile.mkstemp(dir=dirpath, prefix='inv_', suffix='.tmp')
            try:
                with os.fdopen(fd, 'w', encoding='utf-8') as tmpf:
                    json.dump(datos, tmpf, indent=4, ensure_ascii=False)
                    tmpf.flush()
                    os.fsync(tmpf.fileno())
                # Reemplazar de forma atómica
                os.replace(tmp_path, self.archivo)
            finally:
                # Si por alguna razón tmp existe, eliminarlo
                if os.path.exists(tmp_path):
                    try:
                        os.remove(tmp_path)
                    except Exception:
                        pass
        except Exception as e:
            print(f"Error al guardar: {e}")
            raise

    def agregar_producto(self, producto: Producto):
        if producto.id in self.productos:
            raise ValueError(f"El ID {producto.id} ya existe en el inventario.")
        self.productos[producto.id] = producto
        print(f"Producto agregado: {producto}")
        # Guardar cambios
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        try:
            id_int = int(id_producto)
        except (TypeError, ValueError):
            raise ValueError("El ID debe ser un número entero.")
        if id_int in self.productos:
            removed = self.productos.pop(id_int)
            print(f"Producto eliminado: {removed}")
            self.guardar_en_archivo()
            return removed
        else:
            raise KeyError(f"No existe un producto con ID {id_int}.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        try:
            id_int = int(id_producto)
        except (TypeError, ValueError):
            raise ValueError("El ID debe ser un número entero.")
        if id_int not in self.productos:
            raise KeyError(f"No existe un producto con ID {id_int}.")
        prod = self.productos[id_int]
        if nueva_cantidad is not None:
            prod.cantidad = nueva_cantidad
        if nuevo_precio is not None:
            prod.precio = nuevo_precio
        print(f"Producto actualizado: {prod}")
        self.guardar_en_archivo()
        return prod

    def buscar_por_nombre(self, nombre_parcial):
        if not isinstance(nombre_parcial, str):
            raise ValueError("El nombre a buscar debe ser una cadena.")
        query = nombre_parcial.strip().lower()
        resultados = [p for p in self.productos.values() if query in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for p in sorted(self.productos.values(), key=lambda x: x.id):
            print(p)
