import os
from producto import Producto
from inventario import Inventario

def menu() -> None:
    inv = Inventario("inventario.csv")

    while True:
        print("Sistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Recargar desde archivo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                idp = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad (entero): ").strip())
                precio = float(input("Precio (decimal): ").strip())
                inv.anadir_producto(Producto(idp, nombre, cantidad, precio))
            except ValueError:
                print("Entrada inválida: cantidad debe ser entero y precio decimal.")
            input("\nEnter para continuar...")

        elif opcion == "2":
            idp = input("ID a eliminar: ").strip()
            inv.eliminar_producto(idp)
            input("\nEnter para continuar...")

        elif opcion == "3":
            idp = input("ID a actualizar: ").strip()
            txt_cant = input("Nueva cantidad (vacío para no cambiar): ").strip()
            txt_prec = input("Nuevo precio (vacío para no cambiar): ").strip()
            try:
                cantidad = int(txt_cant) if txt_cant else None
                precio = float(txt_prec) if txt_prec else None
                inv.actualizar_producto(idp, cantidad, precio)
            except ValueError:
                print("Entrada inválida: cantidad debe ser entero y precio decimal.")
            input("\nEnter para continuar...")

        elif opcion == "4":
            nombre = input("Buscar por nombre (coincidencia parcial): ").strip()
            resultados = inv.buscar_por_nombre(nombre)
            inv.imprimir_tabla(resultados)
            input("\nEnter para continuar...")

        elif opcion == "5":
            productos = inv.obtener_todos()
            inv.imprimir_tabla(productos)
            input("\nEnter para continuar...")

        elif opcion == "6":
            inv.recargar()
            input("\nEnter para continuar...")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")
            input("\nEnter para continuar...")

if __name__ == "__main__":
    menu()
