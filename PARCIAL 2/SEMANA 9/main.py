# main.py
from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n--- GESTIÓN DE INVENTARIO ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar por Nombre")
    print("5. Mostrar Todo")
    print("6. Salir")
    return input("Seleccione una opción: ")


def ejecutar():
    mi_inventario = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                id_p = int(input("ID único (número): "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario: "))
                nuevo_p = Producto(id_p, nombre, cantidad, precio)
                mi_inventario.añadir_producto(nuevo_p)
            except ValueError:
                print("\n[Error]: Entrada inválida. Use números para ID, Cantidad y Precio.")

        elif opcion == "2":
            try:
                id_p = int(input("Ingrese el ID del producto a eliminar: "))
                mi_inventario.eliminar_producto(id_p)
            except ValueError:
                print("\n[Error]: El ID debe ser un número.")

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto a modificar: "))
                print("Deje en blanco si no desea modificar el campo.")
                cant_str = input("Nueva cantidad: ")
                prec_str = input("Nuevo precio: ")

                cant = int(cant_str) if cant_str else None
                prec = float(prec_str) if prec_str else None

                mi_inventario.actualizar_producto(id_p, cant, prec)
            except ValueError:
                print("\n[Error]: Los valores deben ser numéricos.")

        elif opcion == "4":
            nombre = input("Escriba el nombre (o parte de él) a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
                for r in resultados: print(r)
            else:
                print("\nNo se encontraron productos con ese nombre.")

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("Cerrando sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    ejecutar()