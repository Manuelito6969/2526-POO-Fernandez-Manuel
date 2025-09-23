import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.agregar_tarea)  # Enter = Añadir tarea

        # Botones
        self.btn_add = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_add.grid(row=0, column=1, padx=5)

        self.btn_complete = tk.Button(root, text="Marcar como Completada", command=self.completar_tarea)
        self.btn_complete.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_delete.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.lista.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.lista.bind("<Double-1>", self.completar_tarea)  # Doble clic = completar tarea

        # Diccionario para almacenar estados de las tareas
        self.tareas = {}

    def agregar_tarea(self, event=None):
        tarea = self.entry.get().strip()
        if tarea:
            self.lista.insert(tk.END, tarea)
            self.tareas[tarea] = False  # No completada
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def completar_tarea(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista.get(index)
            if not self.tareas[tarea]:
                self.tareas[tarea] = True
                self.lista.delete(index)
                self.lista.insert(index, f"✔ {tarea}")
            else:
                self.tareas[tarea] = False
                self.lista.delete(index)
                self.lista.insert(index, tarea.replace("✔ ", ""))
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para marcarla.")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista.get(index).replace("✔ ", "")
            del self.tareas[tarea]
            self.lista.delete(index)
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
