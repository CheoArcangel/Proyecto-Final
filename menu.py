import productos
from utils import Fore

def mostrar_menu():
    while True:
        print(Fore.MAGENTA + "\n" + "=" * 50)
        print(Fore.MAGENTA + "            SISTEMA DE GESTION DE INVENTARIO ")
        print(Fore.MAGENTA + "=" * 50)
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")                                                                   

        opcion = input("\nSeleccione una opción (1-7): ").strip()

        if opcion == "1":
            productos.agregar_producto()
        elif opcion == "2":
            productos.ver_productos()
        elif opcion == "3":
            productos.buscar_producto()
        elif opcion == "4":
            productos.actualizar_producto()
        elif opcion == "5":
            productos.eliminar_producto()
        elif opcion == "6":
            productos.reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.GREEN + "\n¡Gracias por usar nuestro sistema! Hasta luego. 👋")
            break
        else:
            print(Fore.RED + "❌ Opción no válida. Debes elegir un número entre el 1 y el 7.")