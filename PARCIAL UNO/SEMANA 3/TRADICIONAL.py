# Programacion Tradicional#
# Función para ingresar temperaturas diarias#

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    print("Programación Tradicional - Promedio semanal del clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
