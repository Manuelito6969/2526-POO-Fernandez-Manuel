class Software:
    """Representa un programa de software."""
    def __init__(self, nombre, version):
        self.nombre = nombre
        self.version = version

    def __str__(self):
        # Muestra una representación legible del objeto Software
        return f'{self.nombre} (v{self.version})'

class Computadora:
    """Representa una computadora con un sistema operativo y software instalado."""
    def __init__(self, marca, modelo, os):
        self.marca = marca
        self.modelo = modelo
        self.os = os
        # Lista para almacenar objetos de la clase Software
        self.software_instalado = []

    def instalar_software(self, programa):
        """Añade un objeto Software a la lista de software_instalado."""
        if isinstance(programa, Software):
            self.software_instalado.append(programa)
            print(f"**{self.modelo}**: Instalado {programa.nombre}.")

    def __str__(self):
        # Muestra la información de la computadora y su software
        software_listado = ", ".join(str(s) for s in self.software_instalado)
        return (f'Computadora {self.marca} {self.modelo} con OS {self.os}.\n'
                f'Software Instalado: {software_listado if software_listado else "Ninguno"}')


# --- Ejecución y Prueba ---

# 1. Creación de objetos de Software
navegador = Software('Navegador Web', 120.0)
editor = Software('Editor de Texto', 4.5)
juego = Software('Juego de Estrategia', 1.0)

# 2. Creación de objetos de Computadora
pc_escritorio = Computadora('Dell', 'XPS 8960', 'Windows 11')
laptop_trabajo = Computadora('Apple', 'MacBook Air M2', 'macOS Sonoma')

# 3. Instalación de software en las computadoras
print("--- Proceso de Instalación ---")
pc_escritorio.instalar_software(navegador)
pc_escritorio.instalar_software(juego)

laptop_trabajo.instalar_software(navegador)
laptop_trabajo.instalar_software(editor)

# 4. Impresión de Resultados
print("\n--- Estado de la PC de Escritorio ---")
print(pc_escritorio)

print("\n--- Estado de la Laptop de Trabajo ---")
print(laptop_trabajo)

print("\n--- Información del Software ---")
print(juego)