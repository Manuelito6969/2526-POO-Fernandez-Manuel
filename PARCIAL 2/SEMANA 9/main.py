from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todo el Inventario")
    print("6. Salir")


def ejecutar():
    mi_inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID único: "))
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                mi_inventario.agregar_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                print("Error: Entrada no válida. Use números para ID, cantidad y precio.")

        elif opcion == "2":
            id_p = int(input("Ingrese el ID a eliminar: "))
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = int(input("ID del producto a actualizar: "))
            print("Presione Enter para omitir un cambio.")
            cant_str = input("Nueva cantidad: ")
            prec_str = input("Nuevo precio: ")

            cant = int(cant_str) if cant_str else None
            prec = float(prec_str) if prec_str else None
            mi_inventario.actualizar_producto(id_p, cant, prec)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se hallaron coincidencias.")

        elif opcion == "5":
            mi_inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar()

