import tkinter as tk
from tkinter import messagebox


class AppTareasAtajos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas con Atajos - Manuel Fernandez")
        self.root.geometry("450x500")

        # --- Interfaz Gráfica ---
        tk.Label(root, text="Tarea nueva (Enter para añadir):").pack(pady=5)
        self.entrada = tk.Entry(root, width=40, font=("Arial", 12))
        self.entrada.pack(pady=10)
        self.entrada.focus_set()  # Poner el foco al iniciar

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50, height=12, font=("Arial", 12), selectmode=tk.SINGLE)
        self.lista.pack(pady=10, padx=20)

        # Botones (Feedback visual y ayuda)
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Añadir (Enter)", command=self.añadir).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Completar (C)", command=self.completar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Eliminar (Del/D)", command=self.eliminar).grid(row=0, column=2, padx=5)

        # --- CONFIGURACIÓN DE ATAJOS DE TECLADO ---
        # Atajo para añadir (solo cuando el foco está en la entrada)
        self.entrada.bind("<Return>", lambda e: self.añadir())

        # Atajos globales (funcionan en toda la ventana)
        self.root.bind("<KeyPress-c>", lambda e: self.completar())
        self.root.bind("<KeyPress-C>", lambda e: self.completar())
        self.root.bind("<Delete>", lambda e: self.eliminar())
        self.root.bind("<KeyPress-d>", lambda e: self.eliminar())
        self.root.bind("<KeyPress-D>", lambda e: self.eliminar())
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    # --- Funcionalidades ---

    def añadir(self):
        tarea = self.entrada.get()
        if tarea:
            self.lista.insert(tk.END, f"[ ] {tarea}")
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea primero.")

    def completar(self):
        try:
            indice = self.lista.curselection()[0]
            texto = self.lista.get(indice)
            if "[ ]" in texto:
                nuevo_texto = texto.replace("[ ]", "[✔]")
                self.lista.delete(indice)
                self.lista.insert(indice, nuevo_texto)
                self.lista.itemconfig(indice, fg="green")  # Feedback visual
            else:
                messagebox.showinfo("Info", "Tarea ya completada.")
        except IndexError:
            pass  # No hacer nada si no hay selección

    def eliminar(self):
        try:
            indice = self.lista.curselection()[0]
            if messagebox.askyesno("Confirmar", "¿Eliminar tarea seleccionada?"):
                self.lista.delete(indice)
        except IndexError:
            pass


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppTareasAtajos(ventana)
    ventana.mainloop()