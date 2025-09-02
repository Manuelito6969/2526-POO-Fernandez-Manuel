# archivo.py
import csv
import os
from typing import List
from producto import Producto

class GestionInventario:
    """
    Manejo simple de persistencia en CSV.
    - cargar() -> List[Producto]
    - guardar(lproducto) -> bool
    Formato CSV: id,nombre,cantidad,precio
    """
    CAMPOS = ["id", "nombre", "cantidad", "precio"]

    def __init__(self):
        self.ruta = "inventario.csv"
        self._verificar_existencia_archivo()

    def _verificar_existencia_archivo(self) -> None:
        if os.path.exists(self.ruta):
            return
        try:
            with open(self.ruta, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                writer.writeheader()
        except Exception as e:
            print(f"No se pudo crear el archivo '{self.ruta}': {e}")

    def cargar(self) -> List[Producto]:
        lproducto: List[Producto] = []
        try:
            with open(self.ruta, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None or any(c not in reader.fieldnames for c in self.CAMPOS):
                    print("Encabezado inválido en el archivo. Se ignora el contenido.")
                    return lproducto
                for idx, row in enumerate(reader, start=2):
                    try:
                        idp = str(row["id"]).strip()
                        nombre = str(row["nombre"]).strip()
                        cantidad = int(row["cantidad"])
                        precio = float(row["precio"])
                        if not idp:
                            raise ValueError("ID vacío")
                        lproducto.append(Producto(idp, nombre, cantidad, precio))
                    except Exception as e:
                        print(f"Fila {idx} inválida: {e}. Saltada.")
        except FileNotFoundError:
            self._asegurar_archivo()
        except PermissionError:
            print(f"Permiso denegado al leer '{self.ruta}'.")
        except Exception as e:
            print(f"Error leyendo '{self.ruta}': {e}")
        return lproducto

    def guardar(self, lproducto: List[Producto]) -> bool:
        try:
            with open(self.ruta, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                writer.writeheader()
                for p in lproducto:
                    writer.writerow({
                        "id": p.get_id(),
                        "nombre": p.get_nombre(),
                        "cantidad": p.get_cantidad(),
                        "precio": p.get_precio()
                    })
            return True
        except PermissionError:
            print(f"Permiso denegado al escribir '{self.ruta}'.")
        except Exception as e:
            print(f"Error escribiendo '{self.ruta}': {e}")
        return False
