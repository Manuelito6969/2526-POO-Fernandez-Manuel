import tkinter as tk
from tkinter import messagebox, ttk
import random


class AsianDramaManagerApp:
    def __init__(self, root):
        """
        Aplicación especializada para gestionar novelas asiáticas con diseño mejorado.

        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title(" Mi Colección de Dramas Asiáticos")  # Título específico

        # Configuración del tamaño y posición inicial de la ventana
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Configurar color de fondo
        self.root.configure(bg='#f8f0ff')

        # Inicializar la lista de dramas con series populares precargadas
        self.dramas_list = [
            {"nombre": "Goblin (Guardian: The Lonely and Great God)", "vista": False, "tipo": "K-Drama", "rating": 4.8},
            {"nombre": "Vincenzo", "vista": False, "tipo": "K-Drama", "rating": 4.7},
            {"nombre": "Hotel del Luna", "vista": False, "tipo": "K-Drama", "rating": 4.6},
            {"nombre": "The King: Eternal Monarch", "vista": False, "tipo": "K-Drama", "rating": 4.3},
            {"nombre": "Eternal Love (Ten Miles of Peach Blossoms)", "vista": False, "tipo": "C-Drama", "rating": 4.8},
            {"nombre": "The Untamed", "vista": False, "tipo": "C-Drama", "rating": 4.9},
            {"nombre": "My Demon", "vista": False, "tipo": "K-Drama", "rating": 4.5},
            {"nombre": "100 Días Mi Príncipe", "vista": False, "tipo": "K-Drama", "rating": 4.4},
            {"nombre": "Cuando la Vida te Da Mandarinas", "vista": False, "tipo": "K-Drama", "rating": 4.2},
            {"nombre": "Bajo el Paraguas de la Reina", "vista": False, "tipo": "K-Drama", "rating": 4.5},
            {"nombre": "El Señor Queen", "vista": False, "tipo": "K-Drama", "rating": 4.7},
            {"nombre": "Amantes de la Luna: Corazón Escarlata Ryeo", "vista": False, "tipo": "K-Drama", "rating": 4.8},
            {"nombre": "La Luna Abrazando al Sol", "vista": False, "tipo": "K-Drama", "rating": 4.6},
            {"nombre": "Amor a la Luz de la Luna", "vista": False, "tipo": "K-Drama", "rating": 4.4},
            {"nombre": "El Afecto del Rey", "vista": False, "tipo": "K-Drama", "rating": 4.3},
            {"nombre": "Alquimia de las Almas", "vista": False, "tipo": "K-Drama", "rating": 4.7},
            {"nombre": "Bon Appétit, Majestad", "vista": False, "tipo": "C-Drama", "rating": 4.1},
        ]

        # Colores para la interfaz
        self.colors = {
            'background': '#f8f0ff',
            'primary': '#8a2be2',
            'secondary': '#da70d6',
            'accent': '#ff69b4',
            'light': '#f5f5f5',
            'dark': '#4b0082',
            'text': '#2c3e50',
            'success': '#2ecc71',
            'warning': '#f39c12',
            'danger': '#e74c3c'
        }

        # Configurar el estilo de los componentes
        self.setup_styles()

        # Crear y colocar los componentes en la ventana
        self.create_widgets()

        # Actualizar la tabla al iniciar
        self.update_dramas_table()

    def setup_styles(self):
        """Configura estilos para los componentes de la interfaz."""
        self.style = ttk.Style()

        # Configurar tema
        self.style.theme_use('clam')

        # Configurar estilos personalizados
        self.style.configure('Title.TLabel',
                             font=('Helvetica', 18, 'bold'),
                             foreground=self.colors['dark'],
                             background=self.colors['background'])

        self.style.configure('Secondary.TLabel',
                             font=('Helvetica', 10),
                             foreground=self.colors['text'],
                             background=self.colors['background'])

        self.style.configure('TButton',
                             font=('Helvetica', 10, 'bold'),
                             background=self.colors['primary'],
                             foreground='white',
                             borderwidth=1)

        self.style.map('TButton',
                       background=[('active', self.colors['secondary'])])

        self.style.configure('Add.TButton',
                             background=self.colors['success'])

        self.style.map('Add.TButton',
                       background=[('active', '#27ae60')])

        self.style.configure('Clear.TButton',
                             background=self.colors['danger'])

        self.style.map('Clear.TButton',
                       background=[('active', '#c0392b')])

        self.style.configure('TEntry',
                             fieldbackground=self.colors['light'],
                             borderwidth=2,
                             relief='solid')

        self.style.configure('TCombobox',
                             fieldbackground=self.colors['light'],
                             background=self.colors['light'])

        self.style.configure('Treeview',
                             background=self.colors['light'],
                             fieldbackground=self.colors['light'],
                             foreground=self.colors['text'],
                             rowheight=25)

        self.style.configure('Treeview.Heading',
                             background=self.colors['primary'],
                             foreground='white',
                             font=('Helvetica', 10, 'bold'))

        self.style.map('Treeview',
                       background=[('selected', self.colors['secondary'])],
                       foreground=[('selected', 'white')])

    def create_widgets(self):
        """Crea y coloca todos los componentes en la ventana."""
        # Marco principal para organizar los elementos
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar expansión de filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)

        # Encabezado con título y descripción
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky=(tk.W, tk.E))
        header_frame.columnconfigure(0, weight=1)

        title_label = ttk.Label(header_frame,
                                text="🎬 Mi Colección de Dramas Asiáticos",
                                style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=(0, 5))

        desc_label = ttk.Label(header_frame,
                               text="Organiza y lleva el control de tus novelas asiáticas favoritas",
                               style='Secondary.TLabel')
        desc_label.grid(row=1, column=0)

        # Separador
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)

        # Panel de entrada de datos
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)
        input_frame.columnconfigure(1, weight=1)

        # Etiqueta y campo de texto para ingresar drama
        drama_label = ttk.Label(input_frame, text="Nueva novela:", style='Secondary.TLabel')
        drama_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 10))

        self.drama_entry = ttk.Entry(input_frame, width=30, font=('Helvetica', 10))
        self.drama_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        self.drama_entry.bind('<Return>', lambda event: self.add_drama())

        # Combobox para seleccionar tipo de drama
        type_label = ttk.Label(input_frame, text="Tipo:", style='Secondary.TLabel')
        type_label.grid(row=0, column=2, sticky=tk.W, pady=5, padx=(0, 10))

        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(input_frame, textvariable=self.type_var,
                                       values=["K-Drama", "C-Drama", "J-Drama", "T-Drama", "Otro"],
                                       width=10, state="readonly", font=('Helvetica', 10))
        self.type_combo.set("K-Drama")
        self.type_combo.grid(row=0, column=3, sticky=tk.W, pady=5, padx=(0, 10))

        # Combobox para seleccionar rating
        rating_label = ttk.Label(input_frame, text="Rating:", style='Secondary.TLabel')
        rating_label.grid(row=0, column=4, sticky=tk.W, pady=5, padx=(0, 10))

        self.rating_var = tk.StringVar()
        self.rating_combo = ttk.Combobox(input_frame, textvariable=self.rating_var,
                                         values=["5.0", "4.5", "4.0", "3.5", "3.0", "2.5", "2.0"],
                                         width=5, state="readonly", font=('Helvetica', 10))
        self.rating_combo.set("4.5")
        self.rating_combo.grid(row=0, column=5, sticky=tk.W, pady=5)

        # Panel de botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)

        # Botón para agregar drama
        self.add_button = ttk.Button(button_frame, text=" Agregar", command=self.add_drama, style='Add.TButton')
        self.add_button.grid(row=0, column=0, padx=(0, 10))

        # Botón para marcar como vista
        self.watched_button = ttk.Button(button_frame, text=" Marcar como Vista", command=self.mark_as_watched)
        self.watched_button.grid(row=0, column=1, padx=(0, 10))

        # Botón para limpiar lista
        self.clear_button = ttk.Button(button_frame, text=" Limpiar Todo", command=self.clear_dramas,
                                       style='Clear.TButton')
        self.clear_button.grid(row=0, column=2, padx=(0, 10))

        # Botón para recomendar aleatorio
        self.random_button = ttk.Button(button_frame, text=" Recomendar Aleatorio", command=self.recommend_random)
        self.random_button.grid(row=0, column=3)

        # Etiqueta para la lista de dramas
        list_label = ttk.Label(main_frame, text="Mi lista de novelas:",
                               font=('Helvetica', 12, 'bold'),
                               foreground=self.colors['dark'],
                               background=self.colors['background'])
        list_label.grid(row=4, column=0, sticky=tk.W, pady=(15, 10))

        # Marco para la lista con barra de desplazamiento
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=5, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Crear Treeview para mostrar los dramas
        columns = ('#', 'Novela', 'Tipo', 'Rating', 'Estado')
        self.dramas_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)

        # Definir encabezados
        self.dramas_tree.heading('#', text='#')
        self.dramas_tree.heading('Novela', text='Novela')
        self.dramas_tree.heading('Tipo', text='Tipo')
        self.dramas_tree.heading('Rating', text='Rating')
        self.dramas_tree.heading('Estado', text='Estado')

        # Ajustar el ancho de las columnas
        self.dramas_tree.column('#', width=40, anchor=tk.CENTER)
        self.dramas_tree.column('Novela', width=350, anchor=tk.W)
        self.dramas_tree.column('Tipo', width=80, anchor=tk.CENTER)
        self.dramas_tree.column('Rating', width=60, anchor=tk.CENTER)
        self.dramas_tree.column('Estado', width=100, anchor=tk.CENTER)

        # Barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.dramas_tree.yview)
        self.dramas_tree.configure(yscrollcommand=scrollbar.set)

        # Colocar Treeview y scrollbar en el marco
        self.dramas_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Panel de estadísticas
        stats_frame = ttk.Frame(main_frame)
        stats_frame.grid(row=6, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(10, 0))

        # Etiqueta de estadísticas
        self.stats_label = ttk.Label(stats_frame, text="", style='Secondary.TLabel')
        self.stats_label.grid(row=0, column=0, sticky=tk.W)

        # Barra de progreso
        self.progress = ttk.Progressbar(stats_frame, mode='determinate', length=200)
        self.progress.grid(row=0, column=1, padx=(20, 0))

        # Etiqueta de estado en la parte inferior
        self.status_label = ttk.Label(main_frame, text="", relief=tk.SUNKEN, style='Secondary.TLabel')
        self.status_label.grid(row=7, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(10, 0))

        # Enlace para selección de dramas
        self.dramas_tree.bind('<<TreeviewSelect>>', self.on_drama_select)
        self.selected_drama = None

    def add_drama(self):
        """
        Agrega el drama ingresado en el campo de texto a la lista.
        Valida que el campo no esté vacío antes de agregar.
        """
        drama = self.drama_entry.get().strip()
        drama_type = self.type_var.get()
        rating = float(self.rating_var.get())

        if not drama:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa el nombre de una novela.")
            self.drama_entry.focus()
            return

        # Agregar drama a la lista
        self.dramas_list.append({"nombre": drama, "vista": False, "tipo": drama_type, "rating": rating})

        # Actualizar la tabla
        self.update_dramas_table()

        # Limpiar campo de entrada y poner foco en él
        self.drama_entry.delete(0, tk.END)
        self.drama_entry.focus()

        # Actualizar estado
        self.status_label.config(text=f" Novela agregada: {drama} ({drama_type}) - Rating: {rating}")

    def clear_dramas(self):
        """Limpia todos los dramas de la lista (excepto los precargados)."""
        if not self.dramas_list:
            messagebox.showinfo("Lista vacía", "No hay novelas para limpiar.")
            return

        # Confirmar antes de limpiar
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar todas las novelas de tu lista?"):
            # Mantener solo las series precargadas
            self.dramas_list = [d for d in self.dramas_list if d["nombre"] in [
                "Goblin (Guardian: The Lonely and Great God)", "Vincenzo", "Hotel del Luna",
                "The King: Eternal Monarch", "Eternal Love (Ten Miles of Peach Blossoms)",
                "The Untamed", "My Demon", "100 Días Mi Príncipe", "Cuando la Vida te Da Mandarinas",
                "Bajo el Paraguas de la Reina", "El Señor Queen", "Amantes de la Luna: Corazón Escarlata Ryeo",
                "La Luna Abrazando al Sol", "Amor a la Luz de la Luna", "El Afecto del Rey",
                "Alquimia de las Almas", "Bon Appétit, Majestad"
            ]]

            self.update_dramas_table()
            self.status_label.config(text=" Todas las novelas adicionales han sido eliminadas")

    def mark_as_watched(self):
        """Marca el drama seleccionado como visto."""
        if not self.selected_drama:
            messagebox.showwarning("Selección requerida", "Por favor, selecciona una novela de la lista.")
            return

        # Encontrar el drama seleccionado y marcarlo como visto
        for i, drama in enumerate(self.dramas_list):
            if drama["nombre"] == self.selected_drama:
                self.dramas_list[i]["vista"] = True
                break

        # Actualizar la tabla
        self.update_dramas_table()
        self.status_label.config(text=f" ¡Novela marcada como vista: {self.selected_drama}!")
        self.selected_drama = None

    def recommend_random(self):
        """Recomienda un drama aleatorio de la lista de no vistos."""
        unwatched = [d for d in self.dramas_list if not d["vista"]]
        if not unwatched:
            messagebox.showinfo("¡Felicidades!", "¡Ya has visto todas tus novelas!")
            return

        random_drama = random.choice(unwatched)
        messagebox.showinfo("Recomendación aleatoria",
                            f"Te recomendamos ver: {random_drama['nombre']}\n"
                            f"Tipo: {random_drama['tipo']}\n"
                            f"Rating: {random_drama['rating']}/5.0")

    def on_drama_select(self, event):
        """Maneja la selección de un drama en la lista."""
        selection = self.dramas_tree.selection()
        if selection:
            item = self.dramas_tree.item(selection[0])
            self.selected_drama = item['values'][1]  # Obtener el nombre del drama

    def update_dramas_table(self):
        """Actualiza la tabla con los dramas actuales de la lista."""
        # Eliminar todos los elementos actuales de la tabla
        for item in self.dramas_tree.get_children():
            self.dramas_tree.delete(item)

        # Insertar los dramas actualizados
        for i, drama in enumerate(self.dramas_list, 1):
            estado = " Vista" if drama["vista"] else " Por ver"
            rating_str = f"{drama['rating']}/5.0"
            self.dramas_tree.insert('', tk.END, values=(i, drama["nombre"], drama["tipo"], rating_str, estado))

        # Actualizar estadísticas
        self.update_stats()

    def update_stats(self):
        """Actualiza las estadísticas y la barra de progreso."""
        if not self.dramas_list:
            self.stats_label.config(text="Lista vacía. Agrega novelas que quieras ver.")
            self.progress['value'] = 0
            return

        total = len(self.dramas_list)
        vistas = sum(1 for drama in self.dramas_list if drama["vista"])
        pendientes = total - vistas
        porcentaje = (vistas / total) * 100 if total > 0 else 0

        self.stats_label.config(text=f"📊 Estadísticas: {vistas} vistas, {pendientes} por ver")
        self.progress['value'] = porcentaje

        # Actualizar mensaje de estado
        if total == 0:
            self.status_label.config(text="Lista vacía. Agrega novelas que quieras ver.")
        elif vistas == total:
            self.status_label.config(text=" ¡Felicidades! Has visto todas tus novelas.")
        else:
            self.status_label.config(text=f" ¡Sigue así! Te faltan {pendientes} novelas por ver.")


def main():
    """Función principal que inicia la aplicación."""
    root = tk.Tk()
    app = AsianDramaManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

#MADELIN IBETH PIANDA ROSADO