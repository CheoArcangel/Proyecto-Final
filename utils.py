from colorama import init, Fore, Style

# Inicializamos colorama para que los colores se reseteen automáticamente
init(autoreset=True)

def preguntar_continuar(accion):
    """Pregunta al usuario si desea repetir una acción o volver al menú."""
    while True:
        respuesta = input(Fore.YELLOW + f"¿Quieres {accion} otro producto o volver al menú? (s/n): ").strip().lower()
        if respuesta == "s":
            return True   
        elif respuesta == "n":
            return False  
        else:
            print(Fore.RED + "❌ Ingresa 's' o 'n' como respuesta.")