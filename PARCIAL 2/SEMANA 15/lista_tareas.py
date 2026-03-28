import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pro - Manuel Fernandez")
        self.root.geometry("480x420")

        # Lista interna de tareas: cada tarea es {'text': str, 'completed': bool}
        self.tasks = []

        # --- Componentes de la Interfaz ---
        # Frame para la entrada y botones
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10, padx=10, fill=tk.X)

        # Campo de entrada
        self.task_entry = tk.Entry(top_frame, width=36, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.task_entry.focus_set()

        # Evento de Teclado: Presionar Enter para añadir tarea
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Botón Añadir
        self.add_button = tk.Button(top_frame, text="Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=(6, 0))

        # Frame para lista y scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Lista de tareas
        self.tasks_listbox = tk.Listbox(list_frame, width=60, height=12, font=("Arial", 12), selectmode=tk.SINGLE,
                                        yscrollcommand=self.scrollbar.set)
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        # Botones inferiores
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(0, 10))

        self.complete_button = tk.Button(btn_frame, text="Marcar como Completada", command=self.toggle_task_completion,
                                         bg="#2196F3", fg="white")
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336",
                                       fg="white")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Eventos adicionales: doble clic para alternar completado
        self.tasks_listbox.bind("<Double-1>", lambda event: self.toggle_task_completion())
        # Tecla Supr (Delete) para eliminar
        self.tasks_listbox.bind("<Delete>", lambda event: self.delete_task())

        # Mensaje inicial (opcional)
        # self._load_sample_tasks()

        # Mantener la vista actualizada
        self.refresh_tasks_listbox()

    # --- Lógica de la aplicación ---

    def add_task(self):
        """Añade una nueva tarea a la lista con validaciones."""
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Atención", "Debes escribir una tarea.")
            return

        # Evitar duplicados (ignorando mayúsculas/minúsculas y espacios)
        normalized = task_text.lower()
        for t in self.tasks:
            if t['text'].lower() == normalized:
                messagebox.showinfo("Info", "Esa tarea ya existe en la lista.")
                self.task_entry.delete(0, tk.END)
                return

        self.tasks.append({'text': task_text, 'completed': False})
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks_listbox()

    def toggle_task_completion(self):
        """Alterna el estado completado de la tarea seleccionada."""
        try:
            index = self.tasks_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista.")
            return

        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        self.refresh_tasks_listbox()

    def delete_task(self):
        """Elimina la tarea seleccionada (con confirmación)."""
        try:
            index = self.tasks_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")
            return

        task_text = self.tasks[index]['text']
        answer = messagebox.askyesno("Confirmar eliminación", f"¿Seguro que deseas eliminar la tarea:\n\n{task_text}")
        if answer:
            del self.tasks[index]
            self.refresh_tasks_listbox()

    def refresh_tasks_listbox(self):
        """Vuelve a pintar la lista en el Listbox según el estado interno."""
        self.tasks_listbox.delete(0, tk.END)
        for i, t in enumerate(self.tasks):
            display = t['text'] + (" (COMPLETADA)" if t['completed'] else "")
            self.tasks_listbox.insert(tk.END, display)
            # Configurar color: gris para completadas
            if t['completed']:
                self.tasks_listbox.itemconfig(i, fg='gray')
            else:
                self.tasks_listbox.itemconfig(i, fg='black')


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()