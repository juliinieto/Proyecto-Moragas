import sqlite3
import os

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS objetos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            imagen TEXT,
            sonido TEXT,
            posicion_x INTEGER,
            posicion_y INTEGER
        )
    ''')
    conn.commit()

def cargar_recurso(ruta_imagen, ruta_sonido, posicion):
    # Supongo que "cargar_recurso" necesita una posición también
    return {"imagen": ruta_imagen, "sonido": ruta_sonido, "posicion": posicion}

# Rutas y posiciones
direcciona_POSICION = (400, 100)
direccionab_POSICION = (400, 400)

# Datos
datos = [
    {"nombre": "ball_image_a", "imagen": "img/pelotaa.png", "sonido": "musica/arriba.wav", "posicion": direcciona_POSICION},
    {"nombre": "ball_image_b", "imagen": "img/pelotab.png", "sonido": "musica/abajo.wav", "posicion": direccionab_POSICION},
]

# Conexión a la base de datos
conn = sqlite3.connect('objetos.db')
crear_tabla(conn)

# Insertar datos en la tabla
for dato in datos:
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO objetos (nombre, imagen, sonido, posicion_x, posicion_y)
        VALUES (?, ?, ?, ?, ?)
    ''', (dato["nombre"], dato["imagen"], dato["sonido"], dato["posicion"][0], dato["posicion"][1]))
    conn.commit()

# Cerrar la conexión a la base de datos
conn.close()
