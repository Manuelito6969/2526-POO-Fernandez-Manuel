import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f4f7")

        # Cargar imagen
        icono = tk.PhotoImage(file="icon.png")

        # Cambiar el icono (True = icono principal de la app)
        root.iconphoto(True, icono)

        # ================= FRAME SUPERIOR =================
        frame_lista = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview (tabla de eventos)
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings", height=10)
        self.tree.heading("Fecha", text="📅 FECHA")
        self.tree.heading("Hora", text="⏰ HORA")
        self.tree.heading("Descripcion", text="📝 DESCRIPCIÓN")

        self.tree.column("Fecha", width=120, anchor="center")
        self.tree.column("Hora", width=100, anchor="center")
        self.tree.column("Descripcion", width=400, anchor="w")

        self.tree.pack(fill="both", expand=True)
        # Rango de horas de 08:00 a 12:00
        for i in range(1, 6):  # 1 al 5
            hora = 7 + i  # empieza en 8 y aumenta de 1 en 1
            hora_formateada = f"{hora:02d}:00"
            descripcion = f"CLASE N. {i}"
            self.tree.insert("", "end", values=("2025-09-18", hora_formateada, descripcion))

        self.tree.insert("", "end", values=("2025-09-18", "18:00", "TUTORIA PROGRAMACION ORIENTADA A OBJETOS"))

        # ================= FRAME DE ENTRADA =================
        frame_form = tk.Frame(root, bg="#f0f4f7")
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Fecha:", bg="#f0f4f7", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_form, width=12, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Hora:", bg="#f0f4f7", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5)
        self.hora_spin = tk.Spinbox(frame_form, from_=0, to=23, width=3, format="%02.0f")
        self.hora_spin.grid(row=0, column=3, padx=2)
        self.minuto_spin = tk.Spinbox(frame_form, from_=0, to=59, width=3, format="%02.0f")
        self.minuto_spin.grid(row=0, column=4, padx=2)

        tk.Label(frame_form, text="Descripción:", bg="#f0f4f7", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(frame_form, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

        # ================= FRAME DE BOTONES =================
        frame_botones = tk.Frame(root, bg="#f0f4f7")
        frame_botones.pack(fill="x", padx=10, pady=10)

        self.btn_agregar = tk.Button(frame_botones, text="➕ Agregar Evento", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.agregar_evento)
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar Seleccionado", bg="#f44336", fg="white", font=("Arial", 10, "bold"), command=self.eliminar_evento)
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_salir = tk.Button(frame_botones, text="❌ Salir", bg="#555", fg="white", font=("Arial", 10, "bold"), command=root.quit)
        self.btn_salir.pack(side="right", padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = f"{self.hora_spin.get()}:{self.minuto_spin.get()}"
        descripcion = self.descripcion_entry.get().strip()

        if not descripcion:
            messagebox.showwarning("Campo vacío", "Debe ingresar una descripción para el evento.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Sin selección", "Debe seleccionar un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            for item in seleccionado:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
