import sqlite3

# Establecer conexión con la base de datos
conn = sqlite3.connect('esquive.db')
cursor = conn.cursor()

# Crear tabla de imágenes si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS imagenes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        ruta TEXT
    )
''')

# Crear tabla de sonidos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sonidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        ruta TEXT
    )
''')

# Insertar datos de imágenes
cursor.executemany('INSERT INTO imagenes (nombre, ruta) VALUES (?, ?)', [
    ('fondo', 'imagenes/lugar.jpg'),
    ('peppa', 'imagenes/peppe.png'),
    ('pelota', 'imagenes/burbuja.png')
])

# Insertar datos de sonidos
cursor.executemany('INSERT INTO sonidos (nombre, ruta) VALUES (?, ?)', [
    ('salto', 'sonidos/arriba.wav'),
    ('fin', 'sonidos/termino.wav')
])

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
