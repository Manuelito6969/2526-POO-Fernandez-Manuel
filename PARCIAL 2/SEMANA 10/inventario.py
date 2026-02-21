import json
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario {id: objeto_producto}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga datos desde JSON con manejo de excepciones."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    for id_p, info in datos.items():
                        # Convertimos los datos del JSON de nuevo a objetos Producto
                        p = Producto(int(id_p), info['nombre'], info['cantidad'], info['precio'])
                        self.productos[int(id_p)] = p
                print(f"--- Inventario cargado desde {self.archivo} ---")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error de acceso al archivo: {e}")
        except json.JSONDecodeError:
            print("Error: El archivo JSON está corrupto. Se iniciará un inventario vacío.")
        except Exception as e:
            print(f"Error inesperado al cargar: {e}")

    def guardar_en_archivo(self):
        """Guarda el diccionario de objetos en formato JSON."""
        try:
            # Convertimos cada objeto Producto a un diccionario simple
            datos_json = {id_p: p.to_dict() for id_p, p in self.productos.items()}
            with open(self.archivo, 'w') as f:
                json.dump(datos_json, f, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: El ID {producto.id} ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_en_archivo()
            print("Producto añadido y sincronizado con el archivo.")

    def eliminar_producto(self, id_p):
        if id_p in self.productos:
            del self.productos[id_p]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: ID no encontrado.")

    def actualizar_producto(self, id_p, cantidad=None, precio=None):
        if id_p in self.productos:
            if cantidad is not None: self.productos[id_p].cantidad = cantidad
            if precio is not None: self.productos[id_p].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos.values():
            print(p)