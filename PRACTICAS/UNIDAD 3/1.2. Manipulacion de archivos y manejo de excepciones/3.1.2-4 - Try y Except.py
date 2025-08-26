try:
    # Intenta ejecutar este bloque de código que puede lanzar excepciones
    resultado = 10 / 0  # Esto provocará un ZeroDivisionError
    #resultado = int("no es un número")  # Descomenta para probar ValueError
except ZeroDivisionError:
    print("Error: División por cero. er1")
except ValueError:
    print("Error: Valor no válido. er c2")
except:
    # Captura cualquier otra excepción no capturada por los except anteriores
    print("Error desconocido. er c3")