from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO (CON JSON) ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todo el Inventario")
    print("6. Salir")
    return input("Seleccione una opción: ")


def ejecutar():
    inv = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                id_p = int(input("ID único (número): "))
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                inv.agregar_producto(Producto(id_p, nom, cant, pre))
            except ValueError:
                print("Error: Entrada inválida. ID y Cantidad deben ser enteros, Precio debe ser decimal.")

        elif opcion == "2":
            try:
                id_p = int(input("ID del producto a eliminar: "))
                inv.eliminar_producto(id_p)
            except ValueError:
                print("Error: Ingrese un ID numérico válido.")

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto: "))
                print("Deje vacío si no desea cambiar el valor.")
                c_str = input("Nueva Cantidad: ")
                p_str = input("Nuevo Precio: ")

                cant = int(c_str) if c_str else None
                prec = float(p_str) if p_str else None
                inv.actualizar_producto(id_p, cant, prec)
            except ValueError:
                print("Error: Valores numéricos incorrectos.")

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = inv.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            inv.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo... ¡Cambios guardados!")
            break


if __name__ == "__main__":
    ejecutar()