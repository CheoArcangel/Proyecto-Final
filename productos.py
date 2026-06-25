import persistencia
from utils import preguntar_continuar, Fore, Style

def agregar_producto():
    while True:
        print(Fore.CYAN + "\n--- AGREGAR PRODUCTO ---")
        nombre = input("Ingrese el nombre: ").strip()
        while not nombre:
            print(Fore.RED + "❌ El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre: ").strip()
            
        descripcion = input("Ingrese una breve descripción: ").strip()
        categoria = input("Ingrese la categoría: ").strip()

        # Validación para asegurar que cantidad y precio sean números
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            precio = float(input("Ingrese el precio: "))
        except ValueError:
            print(Fore.RED + "❌ Error: La cantidad debe ser un número entero y el precio un número válido.")
            continue # Vuelve al inicio del bucle si hay error

        # Guardamos en la base de datos
        query = "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)"
        persistencia.ejecutar_consulta(query, (nombre, descripcion, cantidad, precio, categoria))
        
        print(Fore.GREEN + f"\n✅ Producto '{nombre}' agregado correctamente.")

        if not preguntar_continuar("agregar"):
            break

def ver_productos():
    print(Fore.CYAN + "\n--- LISTA DE PRODUCTOS ---")
    query = "SELECT id, nombre, cantidad, precio, categoria FROM productos"
    productos = persistencia.ejecutar_lectura(query)

    if not productos:
        print(Fore.YELLOW + "No hay productos registrados.")
    else:
        print(Fore.BLUE + f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Cant.':<10} {'Precio':<10}")
        print("-" * 65)
        for prod in productos:
            print(f"{prod[0]:<5} {prod[1]:<20} {prod[4]:<15} {prod[2]:<10} ${prod[3]:<10.2f}")

def buscar_producto():
    while True:
        print(Fore.CYAN + "\n--- BUSCAR PRODUCTO ---")
        busqueda = input("Ingrese el ID, nombre o categoría a buscar: ").strip()
        
        # Buscamos coincidencias en id, nombre o categoria
        query = "SELECT * FROM productos WHERE id = ? OR nombre LIKE ? OR categoria LIKE ?"
        productos = persistencia.ejecutar_lectura(query, (busqueda, f"%{busqueda}%", f"%{busqueda}%"))

        if productos:
            print(Fore.GREEN + f"\n✅ Se encontraron {len(productos)} coincidencia(s):")
            for prod in productos:
                print(Fore.BLUE + f"ID: {prod[0]} | Nombre: {prod[1]} | Categoría: {prod[5]} | Cantidad: {prod[3]} | Precio: ${prod[4]}")
                print(f"Descripción: {prod[2]}\n" + "-"*30)
        else:
            print(Fore.RED + f"\n❌ No se encontró ningún producto relacionado con '{busqueda}'.")
        
        if not preguntar_continuar("buscar"):
            break

def actualizar_producto():
    while True:
        print(Fore.CYAN + "\n--- ACTUALIZAR PRODUCTO ---")
        ver_productos()
        try:
            id_prod = int(input("\nIngrese el ID del producto a actualizar (0 para cancelar): "))
            if id_prod == 0:
                break
            
            # Verificamos si existe
            producto = persistencia.ejecutar_lectura("SELECT * FROM productos WHERE id = ?", (id_prod,))
            if not producto:
                print(Fore.RED + "❌ ID no encontrado.")
                continue

            print(Fore.YELLOW + "Deje el campo vacío si no desea modificarlo.")
            nuevo_nombre = input(f"Nuevo nombre ({producto[0][1]}): ").strip() or producto[0][1]
            nueva_desc = input(f"Nueva descripción ({producto[0][2]}): ").strip() or producto[0][2]
            nueva_cat = input(f"Nueva categoría ({producto[0][5]}): ").strip() or producto[0][5]
            
            # Manejo seguro para números
            nueva_cant_str = input(f"Nueva cantidad ({producto[0][3]}): ").strip()
            nueva_cant = int(nueva_cant_str) if nueva_cant_str else producto[0][3]
            
            nuevo_precio_str = input(f"Nuevo precio ({producto[0][4]}): ").strip()
            nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else producto[0][4]

            # Actualizamos en BD
            query = "UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id=?"
            persistencia.ejecutar_consulta(query, (nuevo_nombre, nueva_desc, nueva_cant, nuevo_precio, nueva_cat, id_prod))
            print(Fore.GREEN + "✅ Producto actualizado con éxito.")

        except ValueError:
            print(Fore.RED + "❌ Por favor, ingrese datos válidos.")
            
        if not preguntar_continuar("actualizar"):
            break

def eliminar_producto():
    while True:
        print(Fore.CYAN + "\n--- ELIMINAR PRODUCTO ---")
        ver_productos()
        try:
            id_prod = int(input("\nIngrese el ID del producto a eliminar (0 para cancelar): "))
            if id_prod == 0:
                break
            
            # Verificamos si existe antes de borrar
            producto = persistencia.ejecutar_lectura("SELECT nombre FROM productos WHERE id = ?", (id_prod,))
            if producto:
                persistencia.ejecutar_consulta("DELETE FROM productos WHERE id = ?", (id_prod,))
                print(Fore.GREEN + f"\n✅ Producto '{producto[0][0]}' (ID: {id_prod}) eliminado correctamente.")
            else:
                print(Fore.RED + "❌ ID no encontrado.")
        except ValueError:
            print(Fore.RED + "❌ Por favor, ingrese un número válido.")

        if not preguntar_continuar("eliminar"):
            break

def reporte_bajo_stock():
    print(Fore.CYAN + "\n--- REPORTE DE BAJO STOCK ---")
    try:
        limite = int(input("Ingrese el límite de cantidad para el reporte: "))
        query = "SELECT id, nombre, cantidad FROM productos WHERE cantidad <= ?"
        productos = persistencia.ejecutar_lectura(query, (limite,))

        if not productos:
            print(Fore.GREEN + f"✅ No hay productos con cantidad igual o menor a {limite}.")
        else:
            print(Fore.YELLOW + f"⚠️  Productos con stock crítico (<= {limite}):")
            print(Fore.BLUE + f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10}")
            print("-" * 40)
            for prod in productos:
                print(f"{prod[0]:<5} {prod[1]:<20} {prod[2]:<10}")
    except ValueError:
        print(Fore.RED + "❌ Por favor, ingrese un número válido.")