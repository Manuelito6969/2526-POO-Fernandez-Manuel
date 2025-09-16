# Sistema GUI básico con Tkinter:
# - Ventana con título
# - Labels, Entry (campo de texto), Botones
# - Tabla para mostrar datos (ttk.Treeview)
# - Funciones: Agregar, Limpiar entrada, Eliminar seleccionado, Limpiar tabla, Salir
# - Manejo de eventos: clic en botones y tecla Enter para agregar

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Datos - Ejemplo GUI con Tkinter")
        self.geometry("640x420")
        self.resizable(False, False)

        # ---------------------------
        # Estado interno
        # ---------------------------
        self.contador_id = 1  # ID incremental para filas
        self.texto_var = tk.StringVar()  # enlaza Entry con variable

        # ---------------------------
        # Construcción de la interfaz
        # ---------------------------
        self._construir_widgets()
        self._configurar_tabla()
        self._configurar_eventos()

    def _construir_widgets(self):
        # Frame superior: entrada y botones de acción
        frm_top = ttk.Frame(self, padding=10)
        frm_top.pack(fill="x")

        lbl_titulo = ttk.Label(frm_top, text="Ingrese un dato para agregar a la tabla:")
        lbl_titulo.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 8))

        ttk.Label(frm_top, text="Texto:").grid(row=1, column=0, sticky="e", padx=(0, 6))
        self.entry_texto = ttk.Entry(frm_top, width=40, textvariable=self.texto_var)
        self.entry_texto.grid(row=1, column=1, sticky="w")

        # Botones principales
        btn_agregar = ttk.Button(frm_top, text="Agregar", command=self.on_agregar)
        btn_agregar.grid(row=1, column=2, padx=8)

        btn_limpiar_entrada = ttk.Button(frm_top, text="Limpiar entrada", command=self.on_limpiar_entrada)
        btn_limpiar_entrada.grid(row=1, column=3)

        # Línea separadora
        ttk.Separator(self, orient="horizontal").pack(fill="x", padx=10, pady=8)

        # Frame central: tabla y barra de scroll
        frm_table = ttk.Frame(self, padding=(10, 0))
        frm_table.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frm_table, columns=("id", "texto"), show="headings", height=11)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scroll vertical
        yscroll = ttk.Scrollbar(frm_table, orient="vertical", command=self.tree.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=yscroll.set)

        # Expansión
        frm_table.columnconfigure(0, weight=1)
        frm_table.rowconfigure(0, weight=1)

        # Frame inferior: acciones sobre tabla y estado
        frm_bottom = ttk.Frame(self, padding=10)
        frm_bottom.pack(fill="x")

        btn_eliminar_sel = ttk.Button(frm_bottom, text="Eliminar seleccionado", command=self.on_eliminar_seleccionado)
        btn_eliminar_sel.grid(row=0, column=0, padx=(0, 8))

        btn_limpiar_tabla = ttk.Button(frm_bottom, text="Limpiar tabla", command=self.on_limpiar_tabla)
        btn_limpiar_tabla.grid(row=0, column=1, padx=(0, 8))

        btn_salir = ttk.Button(frm_bottom, text="Salir", command=self.on_salir)
        btn_salir.grid(row=0, column=2)

        # Label de estado
        self.lbl_estado = ttk.Label(frm_bottom, text="Listo.")
        self.lbl_estado.grid(row=1, column=0, columnspan=3, sticky="w", pady=(8, 0))

    def _configurar_tabla(self):
        # Configura columnas y encabezados
        self.tree.heading("id", text="ID")
        self.tree.heading("texto", text="Texto")
        self.tree.column("id", width=80, anchor="center")
        self.tree.column("texto", width=480, anchor="w")

    def _configurar_eventos(self):
        # Enter en el Entry agrega
        self.entry_texto.bind("<Return>", lambda e: self.on_agregar())
        # Doble clic en una fila muestra el contenido
        self.tree.bind("<Double-1>", self.on_doble_click_fila)

    # ---------------------------
    # Lógica de eventos
    # ---------------------------
    def on_agregar(self):
        texto = self.texto_var.get().strip()
        if not texto:
            messagebox.showwarning("Validación", "Ingrese un texto antes de agregar.")
            self._set_estado("Operación cancelada: texto vacío.")
            return

        # Inserta nueva fila
        self.tree.insert("", "end", values=(self.contador_id, texto))
        self._set_estado(f"Fila agregada con ID {self.contador_id}.")
        self.contador_id += 1
        self.texto_var.set("")  # limpia el campo
        self.entry_texto.focus()

    def on_limpiar_entrada(self):
        self.texto_var.set("")
        self.entry_texto.focus()
        self._set_estado("Entrada limpiada.")

    def on_eliminar_seleccionado(self):
        items = self.tree.selection()
        if not items:
            messagebox.showinfo("Información", "Seleccione una fila para eliminar.")
            return
        for item in items:
            self.tree.delete(item)
        self._set_estado("Fila(s) eliminada(s).")

    def on_limpiar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self._set_estado("Tabla limpiada.")

    def on_doble_click_fila(self, event):
        # Muestra el texto de la fila al hacer doble clic (demostración de manejo de eventos)
        item_id = self.tree.focus()
        if not item_id:
            return
        _, texto = self.tree.item(item_id, "values")
        messagebox.showinfo("Detalle", f"Texto de la fila: {texto}")

    def on_salir(self):
        self.destroy()

    def _set_estado(self, msg: str):
        self.lbl_estado.config(text=msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()
