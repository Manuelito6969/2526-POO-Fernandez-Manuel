import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("850x600")
        self.root.config(bg="#f4f6f9")
        self.root.resizable(False, False)
        self.root.iconphoto(True, tk.PhotoImage(file="icon.png"))

        # === CONTENEDOR PRINCIPAL ===
        frame_main = tk.Frame(self.root, bg="#f4f6f9")
        frame_main.pack(fill="both", expand=True)

        # === FRAME IZQUIERDO (Calendario + Controles) ===
        frame_left = tk.Frame(frame_main, bg="#ffffff", padx=10, pady=10)
        frame_left.pack(side="left", fill="y")

        # --- Calendario ---
        tk.Label(frame_left, text="Selecciona una fecha",
                 font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5, fill="x")

        self.cal = Calendar(frame_left, selectmode="day", date_pattern="yyyy-mm-dd")
        self.cal.pack(pady=10, fill="x")   # 🔹 ocupa todo el ancho del frame_left

        # --- Controles debajo del calendario ---
        frame_controles = tk.LabelFrame(frame_left, text="Nuevo Evento",
                                        bg="#f4f6f9", font=("Arial", 10, "bold"), padx=10, pady=10)
        frame_controles.pack(fill="x", pady=10)   # 🔹 ocupa todo el ancho del frame_left

        # Hora
        tk.Label(frame_controles, text="Hora:", bg="#f4f6f9").grid(row=0, column=0, padx=5, pady=5)
        self.cmb_hora = ttk.Combobox(frame_controles, values=[f"{h:02d}:00" for h in range(8, 21)], width=7)
        self.cmb_hora.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_hora.current(0)

        # Descripción
        tk.Label(frame_controles, text="Descripción:", bg="#f4f6f9").grid(row=1, column=0, padx=5, pady=5)
        self.txt_desc = tk.Entry(frame_controles, width=25)
        self.txt_desc.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Botones
        btn_frame = tk.Frame(frame_controles, bg="#f4f6f9")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.btn_add = tk.Button(btn_frame, text="➕ Agregar", bg="#4CAF50", fg="white",
                                 font=("Arial", 10, "bold"), command=self.agregar_evento)
        self.btn_add.pack(side="left", padx=5)

        self.btn_del = tk.Button(btn_frame, text="❌ Eliminar", bg="#F44336", fg="white",
                                 font=("Arial", 10, "bold"), command=self.eliminar_evento)
        self.btn_del.pack(side="left", padx=5)

        self.btn_salir = tk.Button(btn_frame, text="🚪 Salir", bg="#2196F3", fg="white",
                                   font=("Arial", 10, "bold"), command=self.root.quit)
        self.btn_salir.pack(side="left", padx=5)

        # === FRAME DERECHO (Eventos) ===
        frame_eventos = tk.Frame(frame_main, bg="#ffffff", padx=10, pady=10, relief="groove", bd=2)
        frame_eventos.pack(side="right", fill="both", expand=True)

        tk.Label(frame_eventos, text="Eventos del día",
                 font=("Arial", 12, "bold"), bg="#ffffff").pack(anchor="w")

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings", height=20)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=70, anchor="center")
        self.tree.column("Descripción", width=350, anchor="w")
        self.tree.pack(fill="both", expand=True, pady=10)

    # === MÉTODOS ===
    def agregar_evento(self):
        fecha = self.cal.get_date()
        hora = self.cmb_hora.get()
        desc = self.txt_desc.get()

        if not desc.strip():
            messagebox.showwarning("⚠️ Atención", "Debe ingresar una descripción")
            return

        self.tree.insert("", "end", values=(fecha, hora, desc))
        self.txt_desc.delete(0, tk.END)

    def eliminar_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️ Atención", "Debe seleccionar un evento para eliminar")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            for item in selected:
                self.tree.delete(item)


# === INICIAR APP ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
