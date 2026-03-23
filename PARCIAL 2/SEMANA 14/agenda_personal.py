import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import re
import os
import json

# Intentar importar DateEntry de tkcalendar; si no está disponible, usar un fallback sencillo
try:
    from tkcalendar import DateEntry  # pip install tkcalendar
except Exception:
    class DateEntry(ttk.Entry):
        """Fallback mínimo que expone get() y set_date(date) para compatibilidad."""
        def __init__(self, master=None, **kwargs):
            super().__init__(master)
            # Inicializar con fecha actual en formato dd/mm/yyyy
            self.insert(0, datetime.now().strftime("%d/%m/%Y"))

        def get(self):
            return super().get()

        def set_date(self, date):
            if hasattr(date, 'strftime'):
                s = date.strftime("%d/%m/%Y")
            else:
                s = str(date)
            self.delete(0, tk.END)
            self.insert(0, s)


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal - Manuel Fernandez")
        self.root.geometry("640x520")

        # Archivo de datos (mismo directorio que este archivo)
        self.data_file = os.path.join(os.path.dirname(__file__), 'agenda_data.json')

        # Estado de edición (None cuando no se está editando)
        self.editing_item = None

        # --- 1. FRAME DE ENTRADA DE DATOS ---
        frame_input = tk.LabelFrame(self.root, text="Nuevo Evento", padx=10, pady=10)
        frame_input.pack(pady=10, padx=20, fill="x")

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0, sticky="w")
        self.cal = DateEntry(frame_input, width=12, background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.cal.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Hora (HH:MM):").grid(row=1, column=0, sticky="w")
        self.entry_hora = tk.Entry(frame_input)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0, sticky="w")
        self.entry_desc = tk.Entry(frame_input, width=50)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Atajos: Enter en descripción o hora agrega/guarda
        self.entry_hora.bind('<Return>', lambda e: self.agregar_evento())
        self.entry_desc.bind('<Return>', lambda e: self.agregar_evento())

        # --- 2. FRAME DE BOTONES ---
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=8)

        self.btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento, bg="#4CAF50",
                                     fg="white", width=15)
        self.btn_agregar.pack(side="left", padx=5)

        btn_editar = tk.Button(frame_botones, text="Editar Seleccionado", command=self.editar_evento,
                                bg="#2196F3", fg="white", width=15)
        btn_editar.pack(side="left", padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_evento,
                                  bg="#f44336", fg="white", width=15)
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = tk.Button(frame_botones, text="Salir", command=self.root.quit, width=10)
        btn_salir.pack(side="left", padx=5)

        # --- 3. FRAME DE VISUALIZACIÓN (TREEVIEW) ---
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        # Definición de la Tabla
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=120, anchor="center")
        self.tree.column("Hora", width=90, anchor="center")
        self.tree.column("Descripción", width=380)

        # Añadir scroll
        vsb = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')
        self.tree.pack(fill="both", expand=True)

        # Doble clic para editar rápidamente
        self.tree.bind("<Double-1>", lambda e: self.editar_evento())

        # Mensaje de ayuda
        lbl_help = tk.Label(self.root, text="Doble clic en un evento para editar. Presione Enter para agregar/guardar.")
        lbl_help.pack(pady=4)

        # Cargar eventos guardados si existe el archivo
        self.load_events()

    # --- FUNCIONALIDADES ---

    def validar_hora(self, hora: str) -> bool:
        """Valida formato HH:MM y rango de horas (00:00 - 23:59)."""
        if not hora:
            return False
        pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        return re.match(pattern, hora) is not None

    def _parse_fecha_hora(self, fecha_str: str, hora_str: str):
        """Intenta convertir fecha dd/mm/yyyy y hora HH:MM a datetime; devuelve None si falla."""
        try:
            return datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
        except Exception:
            return None

    def _sort_tree(self):
        """Ordena las filas del Treeview por fecha y hora (ascendente), ignorando filas no parseables."""
        items = []
        for iid in self.tree.get_children(''):
            vals = self.tree.item(iid, 'values')
            if len(vals) >= 2:
                dt = self._parse_fecha_hora(vals[0], vals[1])
                items.append((dt, iid))
            else:
                items.append((None, iid))

        # separar parseables y no parseables
        parseables = [(dt, iid) for dt, iid in items if dt is not None]
        no_parse = [(dt, iid) for dt, iid in items if dt is None]

        parseables.sort(key=lambda x: x[0])

        order = [iid for _, iid in parseables] + [iid for _, iid in no_parse]

        for index, iid in enumerate(order):
            # mover al nuevo índice
            try:
                self.tree.move(iid, '', index)
            except Exception:
                pass

    def agregar_evento(self):
        fecha = self.cal.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        if not hora or not desc:
            messagebox.showwarning("Campos vacíos", "Por favor, complete la hora y la descripción.")
            return

        if not self.validar_hora(hora):
            messagebox.showwarning("Hora inválida", "La hora debe tener el formato HH:MM (00:00 - 23:59).")
            self.entry_hora.focus_set()
            return

        if self.editing_item:
            # Actualizar
            self.tree.item(self.editing_item, values=(fecha, hora, desc))
            self.editing_item = None
            self.btn_agregar.config(text="Agregar Evento", bg="#4CAF50")
        else:
            # Insertar en la tabla
            self.tree.insert("", 'end', values=(fecha, hora, desc))

        # Ordenar después de insertar/editar
        self._sort_tree()

        # Guardar cambios
        self.save_events()

        # Limpiar campos
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.entry_hora.focus_set()

    def eliminar_evento(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Atención", "Seleccione un evento de la lista para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar {len(selected_items)} evento(s)?")
        if not confirm:
            return

        for iid in selected_items:
            try:
                self.tree.delete(iid)
            except Exception:
                pass

        # Si se estaba en edición, cancelar
        if self.editing_item in selected_items:
            self.editing_item = None
            self.btn_agregar.config(text="Agregar Evento", bg="#4CAF50")

        # Guardar cambios
        self.save_events()

    def editar_evento(self):
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Atención", "Seleccione un evento de la lista para editar.")
            return

        iid = selected_items[0]
        vals = self.tree.item(iid, 'values')
        if not vals or len(vals) < 3:
            messagebox.showwarning("Atención", "El evento seleccionado no tiene los datos completos.")
            return

        fecha, hora, desc = vals[0], vals[1], vals[2]

        # Rellenar campos para editar
        try:
            d = datetime.strptime(fecha, "%d/%m/%Y").date()
            try:
                self.cal.set_date(d)
            except Exception:
                # Fallback control DateEntry mínimo puede aceptar string
                self.cal.delete(0, tk.END)
                self.cal.insert(0, fecha)
        except Exception:
            # si no parsea, colocar tal cual
            try:
                self.cal.delete(0, tk.END)
                self.cal.insert(0, fecha)
            except Exception:
                pass

        self.entry_hora.delete(0, tk.END)
        self.entry_hora.insert(0, hora)
        self.entry_desc.delete(0, tk.END)
        self.entry_desc.insert(0, desc)

        self.editing_item = iid
        self.btn_agregar.config(text="Guardar Cambios", bg="#FFA000")

    # --- PERSISTENCIA ---
    def save_events(self):
        """Guarda los eventos visibles en el Treeview a un archivo JSON."""
        events = []
        for iid in self.tree.get_children(''):
            vals = self.tree.item(iid, 'values')
            if not vals or len(vals) < 3:
                continue
            events.append({
                'fecha': vals[0],
                'hora': vals[1],
                'descripcion': vals[2]
            })
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(events, f, ensure_ascii=False, indent=2)
        except Exception:
            # No fatal: mostrar advertencia
            messagebox.showwarning('Error', 'No se pudo guardar el archivo de la agenda.')

    def load_events(self):
        """Carga eventos desde el archivo JSON si existe."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                events = json.load(f)
        except Exception:
            # Si falla la carga, omitimos sin bloquear la app
            return

        # Insertar eventos leídos
        for ev in events:
            fecha = ev.get('fecha', '')
            hora = ev.get('hora', '')
            desc = ev.get('descripcion', '')
            # pequeños filtros: requerir hora y desc
            if not hora or not desc:
                continue
            self.tree.insert('', 'end', values=(fecha, hora, desc))

        # Ordenar tras cargar
        self._sort_tree()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()

