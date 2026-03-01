from producto import Producto
from inventario import Inventario


def mostrar_menu():
    """Muestra las opciones disponibles en la consola."""
    print("\n" + "=" * 40)
    print("  SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("1. Añadir Nuevo Producto")
    print("2. Eliminar Producto por ID")
    print("3. Actualizar Cantidad o Precio")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")
    print("=" * 40)
    return input("Seleccione una opción (1-6): ")


def ejecutar_sistema():
    # Se instancia el inventario (que cargará automáticamente el JSON)
    mi_inventario = Inventario()

    while True:
        try:
            opcion = mostrar_menu()

            if opcion == "1":
                try:
                    print("\n--- Añadir Producto ---")
                    id_p = int(input("ID único (número): "))
                    nombre = input("Nombre del producto: ").strip()
                    cantidad = int(input("Cantidad inicial: "))
                    precio = float(input("Precio unitario: "))

                    nuevo_p = Producto(id_p, nombre, cantidad, precio)
                    mi_inventario.agregar_producto(nuevo_p)
                except ValueError as e:
                    print(f"Error: {e}")

            elif opcion == "2":
                try:
                    id_eliminar = int(input("\nIngrese el ID del producto a eliminar: "))
                    confirm = input(f"¿Confirma eliminar el producto con ID {id_eliminar}? (s/n): ").strip().lower()
                    if confirm == 's':
                        mi_inventario.eliminar_producto(id_eliminar)
                    else:
                        print("Operación cancelada.")
                except ValueError:
                    print("Error: Debe ingresar un número de ID válido.")
                except KeyError as e:
                    print(f"Error: {e}")

            elif opcion == "3":
                try:
                    id_act = int(input("\nID del producto a actualizar: "))
                    print("Deje vacío y presione Enter si no desea cambiar el valor.")
                    can_str = input("Nueva cantidad: ")
                    pre_str = input("Nuevo precio: ")

                    # Solo convertimos si el usuario escribió algo
                    nueva_can = int(can_str) if can_str else None
                    nuevo_pre = float(pre_str) if pre_str else None

                    mi_inventario.actualizar_producto(id_act, nueva_can, nuevo_pre)
                except ValueError as e:
                    print(f"Error: {e}")
                except KeyError as e:
                    print(f"Error: {e}")

            elif opcion == "4":
                nombre_buscar = input("\nIngrese el nombre o parte del nombre a buscar: ")
                resultados = mi_inventario.buscar_por_nombre(nombre_buscar)
                if resultados:
                    print(f"\nResultados encontrados para '{nombre_buscar}':")
                    for prod in resultados:
                        print(prod)
                else:
                    print("No se encontraron productos con ese nombre.")

            elif opcion == "5":
                print("\n--- INVENTARIO COMPLETO ---")
                mi_inventario.mostrar_todos()

            elif opcion == "6":
                print("Guardando cambios y saliendo del sistema... ¡Hasta pronto!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo...")
            break


if __name__ == "__main__":
    ejecutar_sistema()