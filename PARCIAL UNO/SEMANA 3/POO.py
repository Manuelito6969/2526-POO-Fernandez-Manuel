##Orientada a objetos - Promedio semanal del clima##


class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

class ClimaSemanal(ClimaDiario):
    def ingresar_temperaturas_semanales(self):
        for dia in range(7):
            temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.ingresar_temperatura(temp)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Programa principal
def main():
    print("Programación Orientada a Objetos - Promedio semanal del clima")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas_semanales()
    clima.mostrar_promedio()

# Ejecutar el programa
if __name__ == "__main__":
    main()
