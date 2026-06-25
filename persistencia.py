import sqlite3

# Nombre del archivo de la base de datos
DB_NAME = 'inventario.db'

def conectar():
    """Crea y retorna una conexión a la base de datos."""
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    """Crea la tabla productos si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()
    # Ejecutamos código SQL para crear la tabla con los requerimientos pedidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def ejecutar_consulta(query, parametros=()):
    """Ejecuta consultas que modifican datos (INSERT, UPDATE, DELETE)."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(query, parametros)
    conexion.commit()
    conexion.close()

def ejecutar_lectura(query, parametros=()):
    """Ejecuta consultas para leer datos (SELECT) y retorna los resultados."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(query, parametros)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados