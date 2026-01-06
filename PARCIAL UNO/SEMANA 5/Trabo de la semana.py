"""
Programa: Calculadora de Índice de Masa Corporal (IMC)
Descripción: Este programa solicita al usuario sus datos básicos, calcula su IMC
             y determina si el peso es saludable utilizando diferentes tipos de datos.
"""


def calcular_imc(peso_kg, altura_m):
    # Calculamos el IMC usando la fórmula: peso / altura al cuadrado
    # El resultado será un tipo de dato 'float'
    resultado_imc = peso_kg / (altura_m ** 2)
    return resultado_imc


def ejecutar_programa():
    # --- Identificadores en snake_case y tipos de datos ---

    # 1. String (cadena de texto)
    nombre_usuario = input("Introduce tu nombre: ")

    # 2. Float (número decimal)
    peso = float(input("Introduce tu peso en kg (ej. 75.5): "))
    altura = float(input("Introduce tu altura en metros (ej. 1.75): "))

    # 3. Integer (número entero)
    edad = int(input("Introduce tu edad: "))

    # Llamada a la función para procesar datos
    valor_imc = calcular_imc(peso, altura)

    # 4. Boolean (valor lógico)
    # Verificamos si el IMC está en el rango saludable (18.5 - 24.9)
    es_saludable = 18.5 <= valor_imc <= 24.9

    # --- Salida de resultados ---
    print(f"\n--- Resumen para {nombre_usuario} ({edad} años) ---")
    print(f"Tu IMC calculado es: {valor_imc:.2f}")

    if es_saludable:
        print("Estado de salud: El peso se encuentra en el rango normal.")
    else:
        print("Estado de salud: Fuera del rango considerado normal.")

    # Mostrar el tipo de dato de la variable booleana para fines educativos
    print(f"\n[Dato técnico] La variable 'es_saludable' es de tipo: {type(es_saludable)}")


if __name__ == "__main__":
    ejecutar_programa()