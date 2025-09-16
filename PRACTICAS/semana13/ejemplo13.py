import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    etiqueta_resultado.config(text=f"Texto: {entrada.get()}")

def mostrar_seleccion():
    seleccion = combo.get()
    etiqueta_resultado.config(text=f"Seleccionado: {seleccion}")

def mostrar_check():
    estados = []
    if var1.get():
        estados.append("Opción 1")
    if var2.get():
        estados.append("Opción 2")
    etiqueta_resultado.config(text="Checks: " + ", ".join(estados))

def mostrar_radio():
    etiqueta_resultado.config(text=f"Radio: {var_radio.get()}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("500x500")

# Label
tk.Label(ventana, text="Etiqueta (Label)", font=("Arial", 12)).pack(pady=5)

# Entry
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto).pack(pady=5)

# Combobox
combo = ttk.Combobox(ventana, values=["Python", "Java", "C#", "JavaScript"])
combo.set("Selecciona un lenguaje")
combo.pack(pady=5)
tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion).pack(pady=5)

# Checkbuttons
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
tk.Checkbutton(ventana, text="Opción 1", variable=var1, command=mostrar_check).pack()
tk.Checkbutton(ventana, text="Opción 2", variable=var2, command=mostrar_check).pack()

# Radiobuttons
var_radio = tk.StringVar(value="Python")
tk.Radiobutton(ventana, text="Python", variable=var_radio, value="Python", command=mostrar_radio).pack()
tk.Radiobutton(ventana, text="Java", variable=var_radio, value="Java", command=mostrar_radio).pack()

# Listbox
tk.Label(ventana, text="Lista de elementos").pack()
listbox = tk.Listbox(ventana)
for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)

# Treeview (tabla)
tk.Label(ventana, text="Tabla (Treeview)").pack()
tabla = ttk.Treeview(ventana, columns=("Col1", "Col2"), show="headings")
tabla.heading("Col1", text="Nombre")
tabla.heading("Col2", text="Edad")
tabla.insert("", tk.END, values=("Juan", 25))
tabla.insert("", tk.END, values=("Ana", 30))
tabla.insert("", tk.END, values=("Luis", 40))
tabla.pack(pady=5)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado aparecerá aquí", fg="blue")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
