import tkinter as tk
from tkinter import ttk, messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas con Menú de Opciones")
        self.root.resizable(False, False)

        # Cargar imagen
        icono = tk.PhotoImage(file="icon.png")

        # Cambiar el icono (True = icono principal de la app)
        root.iconphoto(True, icono)

        # ==== Frame de grupo para entradas ====
        frame_inputs = ttk.LabelFrame(root, text="Nueva tarea", padding=(15, 10))
        frame_inputs.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

        # Entrada de texto
        self.entry = tk.Entry(frame_inputs, font=("Segoe UI", 10))
        self.entry.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="ew")

        # ComboBox para prioridad
        self.combo_prioridad = ttk.Combobox(frame_inputs, values=["Normal", "Urgente"], state="readonly", width=12, font=("Segoe UI", 10))
        self.combo_prioridad.current(0)
        self.combo_prioridad.grid(row=0, column=1, padx=(0, 10), pady=5)

        # Botón añadir
        self.btn_add = tk.Button(frame_inputs, text="Añadir Tarea", command=self.agregar_tarea, font=("Segoe UI", 10), width=15)
        self.btn_add.grid(row=0, column=2, pady=5)

        frame_inputs.columnconfigure(0, weight=1)

        # ==== Treeview con columna de opciones ====
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)

        self.tree = ttk.Treeview(
            root,
            columns=("Tarea", "Prioridad", "Completada", "Opciones"),
            show="headings",
            height=15
        )
        self.tree.heading("Tarea", text="Tarea")
        self.tree.heading("Prioridad", text="Prioridad")
        self.tree.heading("Completada", text="Completada")
        self.tree.heading("Opciones", text="")

        # Ajuste de columnas
        self.tree.column("Tarea", width=320, anchor="w")
        self.tree.column("Prioridad", width=120, anchor="center")
        self.tree.column("Completada", width=100, anchor="center")
        self.tree.column("Opciones", width=50, anchor="center")

        self.tree.grid(row=1, column=0, padx=15, pady=(0,15))

        # Bindings
        self.entry.bind("<Return>", self.agregar_tarea)
        self.tree.bind("<Button-3>", self.mostrar_menu)   # Clic derecho
        self.tree.bind("<Button-1>", self.click_opciones) # Clic en columna Opciones

        # Menú contextual
        self.menu = tk.Menu(root, tearoff=0)

        # Centrar ventana
        self.centrar_ventana(620, 450)

    def centrar_ventana(self, ancho, alto):
        """Centrar ventana en la pantalla"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def agregar_tarea(self, event=None):
        tarea = self.entry.get().strip()
        prioridad = self.combo_prioridad.get()
        if tarea:
            self.tree.insert("", tk.END, values=(tarea, prioridad, "", "⋮"))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def mostrar_menu(self, event, item=None):
        if not item:
            item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            valores = list(self.tree.item(item, "values"))

            self.menu.delete(0, tk.END)

            if valores[2] == "":  # No completada
                self.menu.add_command(label="Marcar como completada", command=lambda: self.marcar_completada(item))
            else:
                self.menu.add_command(label="Quitar completada", command=lambda: self.quitar_completada(item))

            self.menu.add_separator()
            self.menu.add_command(label="Eliminar", command=lambda: self.eliminar_tarea(item))

            self.menu.tk_popup(event.x_root, event.y_root)

    def click_opciones(self, event):
        col = self.tree.identify_column(event.x)
        item = self.tree.identify_row(event.y)
        if col == "#4" and item:  # Columna Opciones
            self.mostrar_menu(event, item)

    def marcar_completada(self, item):
        valores = list(self.tree.item(item, "values"))
        valores[2] = "✔"
        self.tree.item(item, values=valores)

    def quitar_completada(self, item):
        valores = list(self.tree.item(item, "values"))
        valores[2] = ""
        self.tree.item(item, values=valores)

    def eliminar_tarea(self, item):
        self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
