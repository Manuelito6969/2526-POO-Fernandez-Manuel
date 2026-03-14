import tkinter as tk
from tkinter import messagebox

import json
import os
import logging
from pathlib import Path
from datetime import datetime

# Archivo de datos y configuración
DATA_FILE = Path(__file__).parent / "app_data.json"
LOG_FILE = Path(__file__).parent / "app_gui.log"
MAX_ITEM_LEN = 200

# Configuración básica de logging
logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Datos Básica - Manuel Fernandez")
        self.root.geometry("400x400")

        # --- Componentes GUI ---

        # 1. Etileta (Label)
        self.label_instruccion = tk.Label(root, text="Ingrese un nuevo dato:", font=("Arial", 10))
        self.label_instruccion.pack(pady=10)

        # 2. Campo de Texto (Entry)
        self.entrada_dato = tk.Entry(root, width=35)
        self.entrada_dato.pack(pady=5)

        # 3. Contenedor para Botones (Frame para organizar)
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        # Botón Agregar
        self.boton_agregar = tk.Button(
            self.frame_botones,
            text="Agregar",
            command=self.agregar_dato,
            bg="#4CAF50",
            fg="white",
        )
        self.boton_agregar.grid(row=0, column=0, padx=5)

        # Botón Limpiar (mantiene su función original)
        self.boton_limpiar = tk.Button(
            self.frame_botones,
            text="Limpiar Lista",
            command=self.limpiar_datos,
            bg="#f44336",
            fg="white",
        )
        self.boton_limpiar.grid(row=0, column=1, padx=5)

        # Botón Eliminar selección
        self.boton_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar seleccionado",
            command=self.eliminar_dato,
            bg="#FF9800",
            fg="white",
        )
        self.boton_eliminar.grid(row=0, column=2, padx=5)

        # 4. Lista para mostrar datos (Listbox)
        self.label_lista = tk.Label(root, text="Información Agregada:", font=("Arial", 10, "bold"))
        self.label_lista.pack(pady=5)

        self.lista_datos = tk.Listbox(root, width=50, height=10)
        self.lista_datos.pack(pady=10, padx=20)

        # Barra de estado
        self.status_label = tk.Label(root, text="Listo", bd=1, relief=tk.SUNKEN, anchor="w")
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Datos en memoria
        self.items = []

        # Binds de teclado
        self.root.bind('<Return>', self.agregar_dato)  # Enter para agregar
        self.root.bind('<KP_Enter>', self.agregar_dato)
        self.root.bind('<Delete>', self.eliminar_dato)  # Supr para eliminar
        self.root.bind('<Control-s>', lambda e: self.save_data())  # Ctrl+S guardar

        # Cargar datos persistentes
        try:
            self.items = self.load_data()
            for item in self.items:
                self.lista_datos.insert(tk.END, item)
            self._update_status(f"Cargados {len(self.items)} ítems")
        except Exception as e:
            logger.exception("Error al cargar datos iniciales")
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")

    # --- Funcionalidad y Eventos ---

    def _update_status(self, text: str):
        try:
            self.status_label.config(text=text)
        except Exception:
            logger.exception("Error actualizando status")

    def _normalize(self, text: str) -> str:
        return text.strip()

    def agregar_dato(self, event=None):
        """Evento para el botón Agregar: toma el texto y lo pone en la lista."""
        try:
            dato = self.entrada_dato.get()
            dato_norm = self._normalize(dato)

            if not dato_norm:
                messagebox.showwarning("Advertencia", "El campo de texto está vacío o solo tiene espacios.")
                self._update_status("Entrada vacía")
                return

            if len(dato_norm) > MAX_ITEM_LEN:
                messagebox.showwarning("Advertencia", f"El dato es demasiado largo (máx. {MAX_ITEM_LEN} caracteres).")
                self._update_status("Entrada demasiado larga")
                return

            # Prevención de duplicados (case-insensitive, trim)
            lower_new = dato_norm.casefold()
            for existing in self.items:
                if existing.strip().casefold() == lower_new:
                    messagebox.showinfo("Duplicado", "El dato ya existe en la lista.")
                    self._update_status("Intento de duplicado")
                    return

            # Añadir al estado en memoria y a la UI
            self.items.append(dato_norm)
            self.lista_datos.insert(tk.END, dato_norm)
            self.entrada_dato.delete(0, tk.END)
            self.entrada_dato.focus()

            # Persistir
            self.save_data()
            self._update_status(f"Agregado: '{dato_norm}' ({len(self.items)} ítems)")
            logger.info("Dato agregado: %s", dato_norm)
        except Exception as e:
            logger.exception("Error al agregar dato")
            messagebox.showerror("Error", f"Ocurrió un error al agregar el dato: {e}")

    def eliminar_dato(self, event=None):
        """Evento para eliminar el item seleccionado en la lista."""
        try:
            seleccion = self.lista_datos.curselection()
            if not seleccion:
                self._update_status("Nada seleccionado para eliminar")
                return

            idx = seleccion[0]
            valor = self.lista_datos.get(idx)
            confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar '{valor}'?")
            if not confirmar:
                self._update_status("Eliminación cancelada")
                return

            # Eliminar de UI y memoria
            self.lista_datos.delete(idx)
            # Encontrar y eliminar la primera coincidencia en items
            for i, it in enumerate(self.items):
                if it.strip().casefold() == valor.strip().casefold():
                    del self.items[i]
                    break

            # Persistir
            self.save_data()
            self._update_status(f"Eliminado: '{valor}' ({len(self.items)} ítems restantes)")
            logger.info("Dato eliminado: %s", valor)
        except Exception as e:
            logger.exception("Error al eliminar dato")
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el dato: {e}")

    def limpiar_datos(self):
        """Evento para el botón Limpiar: borra todo el contenido de la lista."""
        try:
            confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que desea borrar toda la lista?")
            if confirmacion:
                self.lista_datos.delete(0, tk.END)
                self.items = []
                self.save_data()
                self._update_status("Lista vaciada")
                logger.info("Lista vaciada por el usuario")
        except Exception as e:
            logger.exception("Error al limpiar datos")
            messagebox.showerror("Error", f"Ocurrió un error al limpiar la lista: {e}")

    # --- Persistencia y utilidades ---

    def load_data(self):
        """Carga la lista desde DATA_FILE. Si está corrupto crea un respaldo y devuelve []."""
        if not DATA_FILE.exists():
            logger.info("Archivo de datos no existe, empezando con lista vacía.")
            return []

        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Asegurar que sea lista de strings
            if not isinstance(data, list):
                logger.warning("Formato inesperado en %s, se esperaba lista." % DATA_FILE)
                messagebox.showwarning("Advertencia", "Archivo de datos con formato inesperado. Se reiniciará la lista.")
                return []

            # Normalizar elementos a str
            result = [str(x) for x in data]
            logger.info("Datos cargados: %d ítems", len(result))
            return result
        except json.JSONDecodeError:
            # Renombrar archivo corrupto con timestamp
            ts = datetime.now().strftime("%Y%m%d%H%M%S")
            backup = DATA_FILE.with_suffix(f".bak.{ts}")
            try:
                os.replace(DATA_FILE, backup)
                logger.warning("Archivo JSON corrupto. Respaldado en %s", backup)
                messagebox.showwarning("Advertencia", f"Archivo de datos corrupto. Se creó respaldo: {backup}")
            except Exception:
                logger.exception("No se pudo respaldar archivo corrupto")
                messagebox.showerror("Error", "El archivo de datos está corrupto y no se pudo respaldar correctamente.")
            return []
        except Exception as e:
            logger.exception("Error leyendo el archivo de datos")
            messagebox.showerror("Error", f"No se pudo leer el archivo de datos: {e}")
            return []

    def save_data(self):
        """Guarda la lista en DATA_FILE de forma atómica.

        Escribe en un archivo temporal y luego reemplaza el original.
        """
        try:
            tmp_path = DATA_FILE.with_suffix('.tmp')
            with open(tmp_path, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=2)

            # Reemplazo atómico
            os.replace(tmp_path, DATA_FILE)
            logger.info("Datos guardados: %d ítems", len(self.items))
            self._update_status(f"Guardado ({len(self.items)} ítems)")
        except Exception as e:
            logger.exception("Error guardando datos")
            messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")
            self._update_status("Error al guardar datos")


# Configuración de la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionGUI(ventana)
    ventana.mainloop()

