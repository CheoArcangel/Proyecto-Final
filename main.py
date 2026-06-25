import persistencia
import menu

def main():
    # 1. Asegurarnos de que la base de datos y la tabla existan al iniciar
    persistencia.crear_tabla()
    
    # 2. Iniciar la interfaz de usuario
    menu.mostrar_menu()

if __name__ == "__main__":
    main()