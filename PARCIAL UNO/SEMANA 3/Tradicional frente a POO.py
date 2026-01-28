# Programa: Promedios de temperatura semanal
# Comparación: Programación tradicional vs Programación orientada a objetos (POO)

# ----------------------
# Versión tradicional
# ----------------------

# Lista de temperaturas de la semana (lunes a domingo)
temperaturas = [20.5, 22.0, 19.8, 21.0, 23.4, 18.9, 20.0]

def promedio(lista):
    """Devuelve el promedio de una lista de números o None si la lista está vacía."""
    if not lista:
        return None
    return sum(lista) / len(lista)

def minimo(lista):
    """Devuelve el valor mínimo o None si la lista está vacía."""
    if not lista:
        return None
    return min(lista)

def maximo(lista):
    """Devuelve el valor máximo o None si la lista está vacía."""
    if not lista:
        return None
    return max(lista)

# Uso de las funciones (programación tradicional)
prom = promedio(temperaturas)
min_t = minimo(temperaturas)
max_t = maximo(temperaturas)

print("--- Versión tradicional ---")
if prom is None:
    print("No hay temperaturas registradas.")
else:
    print(f"Temperaturas: {temperaturas}")
    print(f"Promedio semanal: {prom:.2f} °C")
    print(f"Mínima: {min_t:.2f} °C")
    print(f"Máxima: {max_t:.2f} °C")


# ----------------------
# Versión orientada a objetos (POO)
# ----------------------

class SemanaTemperaturas:
    """Clase que representa las temperaturas de una semana y ofrece operaciones comunes."""
    def __init__(self, temperaturas=None):
        # Guardamos una copia para evitar efectos secundarios si se pasa la misma lista
        self.temperaturas = list(temperaturas) if temperaturas else []

    def agregar(self, temp):
        """Agrega una temperatura (float o int)."""
        try:
            valor = float(temp)
        except (TypeError, ValueError):
            raise ValueError("La temperatura debe ser un número")
        self.temperaturas.append(valor)

    def promedio(self):
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)

    def minimo(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maximo(self):
        return max(self.temperaturas) if self.temperaturas else None

    def resumen(self):
        """Devuelve un diccionario con estadísticas útiles."""
        return {
            'temperaturas': list(self.temperaturas),
            'promedio': self.promedio(),
            'minimo': self.minimo(),
            'maximo': self.maximo()
        }


# Uso de la clase (POO)
semana = SemanaTemperaturas([20.5, 22.0, 19.8, 21.0, 23.4, 18.9, 20.0])
# También se puede agregar día a día: semana.agregar(21.2)

res = semana.resumen()

print("\n--- Versión POO ---")
if res['promedio'] is None:
    print("No hay temperaturas registradas en la semana (POO).")
else:
    print(f"Temperaturas (POO): {res['temperaturas']}")
    print(f"Promedio semanal (POO): {res['promedio']:.2f} °C")
    print(f"Mínima (POO): {res['minimo']:.2f} °C")
    print(f"Máxima (POO): {res['maximo']:.2f} °C")


# Punto de entrada para ejecutar el archivo directamente
if __name__ == '__main__':
    # Ya hemos mostrado un ejemplo automático arriba; aquí podríamos agregar pruebas rápidas o interacción.
    pass
