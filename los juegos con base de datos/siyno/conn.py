import sqlite3

def crear_tabla_elementos():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect("elementos.db")
        cursor = conn.cursor()

        # Crear la tabla de elementos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS elementos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                tipo TEXT,
                ruta TEXT
            )
        ''')
        # Commit para aplicar los cambios
        conn.commit()
    except sqlite3.Error as e:
        print("Error al crear la tabla de elementos:", e)
    finally:
        # Cerrar la conexión
        if conn:
            conn.close()

def insertar_datos_elementos():
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect("elementos.db")
        cursor = conn.cursor()

        # Insertar datos en la tabla de elementos
        cursor.executemany('''
            INSERT INTO elementos (nombre, tipo, ruta) VALUES (?, ?, ?)
        ''', [
            ('si', 'imagen', 'si.png'),
            ('no', 'imagen', 'no.png'),
            ('si', 'sonido', 'si.wav'),
            ('no', 'sonido', 'no.wav')
        ])

        # Commit para aplicar los cambios
        conn.commit()
    except sqlite3.Error as e:
        print("Error al insertar datos en la tabla de elementos:", e)
    finally:
        # Cerrar la conexión
        if conn:
            conn.close()

# Llama a las funciones para crear la tabla e insertar datos
crear_tabla_elementos()
insertar_datos_elementos()
