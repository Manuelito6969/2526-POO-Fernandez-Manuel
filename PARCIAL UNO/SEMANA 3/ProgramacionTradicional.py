"""
PROGRAMACIÓN TRADICIONAL
Programa para calcular el promedio semanal de temperaturas
Autor: Estudiante UEA - TICs
Asignatura: Programación Orientada a Objetos
"""


def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.

    Returns:
        list: Lista con las temperaturas de los 7 días de la semana
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("=" * 50)
    print("INGRESO DE TEMPERATURAS DIARIAS")
    print("=" * 50)

    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor ingrese un valor numérico válido.")

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de temperaturas.

    Args:
        temperaturas (list): Lista de temperaturas diarias

    Returns:
        float: Promedio de las temperaturas
    """
    if len(temperaturas) == 0:
        return 0

    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def mostrar_resultados(temperaturas, promedio):
    """
    Función para mostrar los resultados del análisis de temperaturas.

    Args:
        temperaturas (list): Lista de temperaturas diarias
        promedio (float): Promedio calculado de temperaturas
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("\n" + "=" * 50)
    print("RESULTADOS DEL ANÁLISIS SEMANAL")
    print("=" * 50)

    print("\nTemperaturas registradas:")
    for i, dia in enumerate(dias_semana):
        print(f"  {dia:12} : {temperaturas[i]:6.2f} °C")

    print("\n" + "-" * 50)
    print(f"Promedio semanal: {promedio:.2f} °C")

    # Información adicional
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    dia_max = dias_semana[temperaturas.index(temp_max)]
    dia_min = dias_semana[temperaturas.index(temp_min)]

    print(f"Temperatura máxima: {temp_max:.2f} °C ({dia_max})")
    print(f"Temperatura mínima: {temp_min:.2f} °C ({dia_min})")
    print("=" * 50)


def menu_principal():
    """
    Función principal que controla el flujo del programa.
    Permite realizar múltiples análisis de temperatura.
    """
    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE ANÁLISIS DE TEMPERATURA SEMANAL")
        print("Programación Tradicional")
        print("=" * 50)
        print("1. Ingresar temperaturas y calcular promedio")
        print("2. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Proceso principal
            temperaturas = ingresar_temperaturas()
            promedio = calcular_promedio(temperaturas)
            mostrar_resultados(temperaturas, promedio)

        elif opcion == "2":
            print("\n¡Gracias por usar el sistema!")
            print("Programa finalizado.")
            break

        else:
            print("\nOpción no válida. Por favor seleccione 1 o 2.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()