import pygame
import sqlite3
import os
import random

pygame.init()

ANCHO = 800
ALTO = 600
IMAGEN_ANCHO = 100
IMAGEN_ALTO = 100

IMG = (IMAGEN_ANCHO, IMAGEN_ALTO)
FONDO_TAMAÑO = (ANCHO, ALTO)

# Conexión a la base de datos
conn = sqlite3.connect('objetos.db')
cursor = conn.cursor()

# Función para cargar los recursos desde la base de datos
def cargar_recursos():
    cursor.execute('SELECT nombre, imagen, sonido, posicion_x, posicion_y FROM objetos')
    recursos = {}
    for row in cursor.fetchall():
        nombre, imagen, sonido, posicion_x, posicion_y = row
        posicion = (posicion_x, posicion_y)
        recursos[nombre] = {"imagen": imagen, "sonido": sonido, "posicion": posicion}
    return recursos

# Carga los recursos desde la base de datos
direccion = cargar_recursos()

# Carga el fondo
FONDO = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "img/fondo.jpg"))
FONDO = pygame.transform.scale(FONDO, FONDO_TAMAÑO)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de direcciones")

direccion_actual = random.choice(list(direccion.keys()))
mostrar_bien_hecho = False
tecla_enter_presionada = False

running = True

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not tecla_enter_presionada:
                    direccion_actual = random.choice(list(direccion.keys()))
                    direccion_sound = pygame.mixer.Sound(direccion[direccion_actual]["sonido"])
                    direccion_sound.play()
                    tecla_enter_presionada = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    tecla_enter_presionada = False

        pantalla.blit(FONDO, (0, 0))
        pantalla.blit(pygame.transform.scale(pygame.image.load(direccion[direccion_actual]["imagen"]), IMG),
                      direccion[direccion_actual]["posicion"])

        pygame.display.flip()

except Exception as e:
    print("An error occurred:", e)

finally:
    # Cierra la conexión a la base de datos
    conn.close()

    pygame.mixer.music.stop()
    pygame.quit()
