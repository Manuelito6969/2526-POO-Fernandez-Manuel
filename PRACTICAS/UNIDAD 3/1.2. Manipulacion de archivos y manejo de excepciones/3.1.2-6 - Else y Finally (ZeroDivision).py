try:
    # Intenta ejecutar este bloque de código
    resultado = 10 / 0
except Exception as error:
    print(f"Error en mi codigo clase sabado: {error}")
else:
    # Este bloque se ejecuta si no hay excepciones en el bloque try
    print("División realizada exitosamente.")
finally:
    # Este bloque se ejecuta siempre, haya o no una excepción
    print("Operación de división finalizada.")