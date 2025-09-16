import tkinter as tk

def agregar():
    texto = entrada.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)

def limpiar():
    entrada.delete(0, tk.END)
    lista.delete(0, tk.END)

root = tk.Tk()
root.title("TAREA SEMANA 13")
#root.iconbitmap("icono.ico")

# Definir tamaño (ancho x alto)
#root.geometry("500x300")

# --- Definir tamaño de la ventana ---
ancho_ventana = 500
alto_ventana = 300

# --- Obtener tamaño de la pantalla ---
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# --- Calcular posición x, y ---
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# --- Definir geometría con tamaño + posición ---
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Cargar imagen
icono = tk.PhotoImage(file="icono.png")

# Cambiar el icono (True = icono principal de la app)
root.iconphoto(True, icono)

tk.Label(root, text="Ingrese un texto:").pack()
entrada = tk.Entry(root)
entrada.pack()

tk.Button(root, text="Agregar", command=agregar).pack()
tk.Button(root, text="Limpiar", command=limpiar).pack()

lista = tk.Listbox(root, width=40)
lista.pack()

root.mainloop()