import tkinter as tk
from tkinter import ttk, messagebox

class PantallaProductos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Productos")
        self.geometry("850x540")
        self.resizable(False, False)

        # Productos fijos
        self.lproducto = [
            {"id": "1", "nombre": "Camisa", "cantidad": 10, "precio": 25.5},
            {"id": "2", "nombre": "Pantalón", "cantidad": 15, "precio": 35.0},
        ]

        # Buscar
        frame_top = tk.Frame(self)
        frame_top.pack(fill="x", padx=10, pady=10)
        tk.Label(frame_top, text="Buscar:").pack(side="left")
        self.entry_buscar = tk.Entry(frame_top, width=30)
        self.entry_buscar.pack(side="left", padx=5)
        tk.Button(frame_top, text="Buscar", command=self.buscar_producto).pack(side="left")
        self.entry_buscar.bind("<Return>", lambda e: self.buscar_producto())

        # Tabla
        columnas = ("Código", "Nombre", "Cantidad", "Precio", "Opciones")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings", height=10)

        for col in columnas[:-1]:
            self.tree.heading(col, text=col)

        self.tree.column("Código", width=120, anchor="center")
        self.tree.column("Nombre", width=250, anchor="w")
        self.tree.column("Cantidad", width=120, anchor="center")
        self.tree.column("Precio", width=120, anchor="center")
        self.tree.column("Opciones", width=50, anchor="center", stretch=False)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Menú contextual
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Editar", command=self.editar_producto)
        self.menu.add_command(label="Eliminar", command=self.eliminar_producto)
        self.tree.bind("<Button-1>", self.click_opciones)

        self.refrescar_treeview()

    def click_opciones(self, event):
        if self.tree.identify_column(event.x) == "#5":  # Columna Opciones
            row_id = self.tree.identify_row(event.y)
            if row_id:
                self.tree.selection_set(row_id)
                self.menu.post(event.x_root, event.y_root)
                return "break"

    def refrescar_treeview(self, lista=None):
        self.tree.delete(*self.tree.get_children())
        for p in (lista if lista else self.lproducto):
            self.tree.insert(
                "",
                tk.END,
                values=(p["id"], p["nombre"], p["cantidad"], p["precio"], "⋮")  # 3 puntos centrados
            )

    def buscar_producto(self):
        texto = self.entry_buscar.get().strip().lower()
        if not texto:
            self.refrescar_treeview()
            return
        filtrados = [p for p in self.lproducto if texto in p["id"].lower() or texto in p["nombre"].lower()]
        if filtrados:
            self.refrescar_treeview(filtrados)
        else:
            messagebox.showinfo("Búsqueda", f"No se encontró '{texto}'.")

    def editar_producto(self):
        sel = self.tree.selection()
        if sel:
            valores = self.tree.item(sel[0], "values")
            messagebox.showinfo("Editar", f"Editar: {valores[1]}")

    def eliminar_producto(self):
        sel = self.tree.selection()
        if sel:
            valores = self.tree.item(sel[0], "values")
            messagebox.showinfo("Eliminar", f"Eliminar: {valores[1]}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    PantallaProductos(root).mainloop()
