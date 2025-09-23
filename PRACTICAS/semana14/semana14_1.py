# agenda_tkinter.py
import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

# Intentar usar tkcalendar.DateEntry; si no está instalado, fallback a Entry para fecha
try:
    from tkcalendar import DateEntry
    HAS_TKCALENDAR = True
except Exception:
    HAS_TKCALENDAR = False

# ------------------ Utilidades ------------------
def centrar_ventana(root, ancho, alto):
    """Centra la ventana en la pantalla."""
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    root.geometry(f"{ancho}x{alto}+{x}+{y}")

def validar_hora(hora_texto):
    """Valida formato HH:MM (24h)."""
    if not re.fullmatch(r"[0-2]\d:[0-5]\d", hora_texto):
        return False
    hh = int(hora_texto.split(":")[0])
    return 0 <= hh <= 23

def parse_fecha_str(fecha_texto):
    """Intenta parsear fecha en 'YYYY-MM-DD' o devuelve None."""
    try:
        return datetime.strptime(fecha_texto, "%Y-%m-%d").date()
    except Exception:
        return None

# ------------------ Clase de la App ------------------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        root.title("Agenda Personal - Tkinter")
        root.minsize(650, 380)
        centrar_ventana(root, 800, 500)

        # Datos en memoria (lista de dicts)
        self.eventos = []

        # --- Frames principales ---
        self.frame_lista = ttk.Frame(root, padding=(10,10))
        self.frame_form = ttk.Frame(root, padding=(10,10))
        self.frame_acciones = ttk.Frame(root, padding=(10,10))

        self.frame_lista.grid(row=0, column=0, sticky="nsew")
        self.frame_form.grid(row=1, column=0, sticky="ew")
        self.frame_acciones.grid(row=2, column=0, sticky="ew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # --- Treeview (lista de eventos) ---
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings", selectmode="browse")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=120, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=500, anchor="w")

        # Scrollbar vertical
        vsb = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        self.frame_lista.grid_rowconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(0, weight=1)

        # --- Formulario de entrada ---
        lbl_fecha = ttk.Label(self.frame_form, text="Fecha:")
        lbl_hora = ttk.Label(self.frame_form, text="Hora (HH:MM):")
        lbl_desc = ttk.Label(self.frame_form, text="Descripción:")

        lbl_fecha.grid(row=0, column=0, padx=5, pady=6, sticky="e")
        lbl_hora.grid(row=0, column=2, padx=5, pady=6, sticky="e")
        lbl_desc.grid(row=1, column=0, padx=5, pady=6, sticky="ne")

        # Widget fecha: DateEntry si tkcalendar está disponible, si no Entry
        if HAS_TKCALENDAR:
            self.entry_fecha = DateEntry(self.frame_form, date_pattern="yyyy-mm-dd")
        else:
            self.entry_fecha = ttk.Entry(self.frame_form)
            self.entry_fecha.insert(0, "YYYY-MM-DD")  # placeholder

        self.entry_hora = ttk.Entry(self.frame_form, width=10)
        self.text_desc = tk.Text(self.frame_form, height=4, width=60)

        self.entry_fecha.grid(row=0, column=1, padx=5, pady=6, sticky="w")
        self.entry_hora.grid(row=0, column=3, padx=5, pady=6, sticky="w")
        self.text_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=6, sticky="w")

        # --- Botones de acción ---
        btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.root.quit)

        btn_agregar.grid(row=0, column=0, padx=10, pady=8, sticky="w")
        btn_eliminar.grid(row=0, column=1, padx=10, pady=8, sticky="w")
        btn_salir.grid(row=0, column=2, padx=10, pady=8, sticky="e")

        self.frame_acciones.grid_columnconfigure(2, weight=1)

        # Doble click en fila para mostrar detalles (opcional)
        self.tree.bind("<Double-1>", self.on_doble_click)

        # Insertar algunos datos de ejemplo
        self.insertar_evento_en_lista("2025-09-20", "09:00", "Cita con el dentista")
        self.insertar_evento_en_lista("2025-09-21", "14:30", "Reunión proyecto MONITOEX")

        self.actualizar_treeview()

    # ---------- Métodos de manejo ----------
    def agregar_evento(self):
        # Obtener valores
        if HAS_TKCALENDAR:
            fecha = self.entry_fecha.get_date().isoformat()
        else:
            fecha = self.entry_fecha.get().strip()

        hora = self.entry_hora.get().strip()
        descripcion = self.text_desc.get("1.0", "end").strip()

        # Validaciones
        if not fecha:
            messagebox.showerror("Error", "La fecha es requerida.")
            return

        if not HAS_TKCALENDAR:
            # validar formato YYYY-MM-DD
            if parse_fecha_str(fecha) is None:
                messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
                return

        if not hora or not validar_hora(hora):
            messagebox.showerror("Error", "Hora inválida. Use formato HH:MM (24 horas).")
            return

        if not descripcion:
            messagebox.showerror("Error", "La descripción no puede estar vacía.")
            return

        # Agregar
        self.insertar_evento_en_lista(fecha, hora, descripcion)
        self.actualizar_treeview()
        self.limpiar_formulario()

    def insertar_evento_en_lista(self, fecha, hora, descripcion):
        evento = {"fecha": fecha, "hora": hora, "descripcion": descripcion}
        self.eventos.append(evento)

    def actualizar_treeview(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insertar ordenado por fecha+hora (simple)
        try:
            eventos_ordenados = sorted(self.eventos, key=lambda e: (e["fecha"], e["hora"]))
        except Exception:
            eventos_ordenados = list(self.eventos)
        for i, ev in enumerate(eventos_ordenados):
            self.tree.insert("", "end", iid=str(i), values=(ev["fecha"], ev["hora"], ev["descripcion"]))

    def limpiar_formulario(self):
        if HAS_TKCALENDAR:
            # DateEntry vuelve al día actual: no hacemos nada especial aquí
            pass
        else:
            self.entry_fecha.delete(0, "end")
        self.entry_hora.delete(0, "end")
        self.text_desc.delete("1.0", "end")

    def eliminar_evento(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Información", "Seleccione un evento para eliminar.")
            return
        item_id = sel[0]
        valores = self.tree.item(item_id, "values")
        fecha, hora, descripcion = valores

        # Confirmación
        confirmar = messagebox.askyesno("Confirmar eliminación",
                                        f"¿Eliminar el evento:\n\nFecha: {fecha}\nHora: {hora}\nDescripción: {descripcion[:60]}?")
        if not confirmar:
            return

        # Buscar y eliminar el primer evento que coincida
        eliminado = False
        for ev in self.eventos:
            if ev["fecha"] == fecha and ev["hora"] == hora and ev["descripcion"] == descripcion:
                self.eventos.remove(ev)
                eliminado = True
                break
        if eliminado:
            self.actualizar_treeview()
            messagebox.showinfo("Eliminado", "Evento eliminado correctamente.")
        else:
            messagebox.showwarning("No encontrado", "No se pudo encontrar el evento para eliminar.")

    def on_doble_click(self, event):
        item = self.tree.identify_row(event.y)
        if not item:
            return
        valores = self.tree.item(item, "values")
        fecha, hora, descripcion = valores
        messagebox.showinfo("Detalles del Evento",
                            f"Fecha: {fecha}\nHora: {hora}\n\nDescripción:\n{descripcion}")

# ------------------ Ejecutar app ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
