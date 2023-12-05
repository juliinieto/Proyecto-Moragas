import pygame
import sys
import random
import sqlite3

# Inicialización de Pygame
pygame.init()

# Establecer conexión con la base de datos
conn = sqlite3.connect('esquive.db')
cursor = conn.cursor()

# Obtener rutas de imágenes y sonidos desde la base de datos
cursor.execute('SELECT nombre, ruta FROM imagenes')
imagenes = dict(cursor.fetchall())

cursor.execute('SELECT nombre, ruta FROM sonidos')
sonidos = dict(cursor.fetchall())

# Pantalla
ANCHO, ALTO = 990, 335
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Supervivencia")

# Cargar imágenes
fondo = pygame.image.load(imagenes['fondo']).convert()
peppa = pygame.image.load(imagenes['peppa']).convert_alpha()
peppa = pygame.transform.scale(peppa, (60, 60))

pelota = pygame.image.load(imagenes['pelota']).convert_alpha()
pelota = pygame.transform.scale(pelota, (34, 34))

# Cargar sonido
sonido_salto = pygame.mixer.Sound(sonidos['salto'])
sonido_fin = pygame.mixer.Sound(sonidos['fin'])

# Función para reiniciar el juego
def reiniciar_juego():
    return {
        'x_peppa': 0,
        'y_peppa': 300,
        'velocidad_salto': 7,  # Aumentado para un salto más alto
        'salto_actual': 0,
        'en_suelo': True,
        'x_pelota': ANCHO,
        'y_pelota': random.randint(50, ALTO - 50),
        'velocidad_pelota': 5,
        'x_fondo': 0,
        'tiempo_actual': 0
    }

# Posiciones iniciales
juego_inicial = reiniciar_juego()
x_peppa, y_peppa = juego_inicial['x_peppa'], juego_inicial['y_peppa']
velocidad_salto = juego_inicial['velocidad_salto']
salto_actual = juego_inicial['salto_actual']
en_suelo = juego_inicial['en_suelo']

# Pelota
x_pelota, y_pelota = juego_inicial['x_pelota'], juego_inicial['y_pelota']
velocidad_pelota = juego_inicial['velocidad_pelota']

# Fondo
x_fondo = juego_inicial['x_fondo']

# Tiempo
tiempo_limite = 3600  # 1 minutos en frames
tiempo_actual = juego_inicial['tiempo_actual']

# Bucle de juego
reloj = pygame.time.Clock()

while tiempo_actual < tiempo_limite:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and en_suelo:
                sonido_salto.play()  # Reproducir sonido de salto
                salto_actual = 0
                en_suelo = False
            elif event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()

    # Mover fondo
    x_fondo -= 1
    x_fondo_rel = x_fondo % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_fondo_rel - fondo.get_rect().width, 0))
    if x_fondo_rel < ANCHO:
        PANTALLA.blit(fondo, (x_fondo_rel, 0))

    # Mover peppa hacia arriba con la tecla Enter (saltar)
    if not en_suelo:
        y_peppa -= velocidad_salto
        salto_actual += 1
        if salto_actual > 17:  # Ajustado para un salto más alto
            en_suelo = True
    else:
        # Caída más lenta
        y_peppa += 3

    # Mover pelota y reiniciar si se sale de la pantalla
    x_pelota -= velocidad_pelota
    if x_pelota < 0:
        x_pelota = ANCHO
        y_pelota = random.randint(50, ALTO - 50)

    # Limitar la posición de Peppa Pig para que no salga de la pantalla
    x_peppa = max(0, min(x_peppa, ANCHO - peppa.get_width()))
    y_peppa = max(0, min(y_peppa, ALTO - peppa.get_height()))

    # Limitar la posición de la pelota para que no salga de la pantalla
    x_pelota = max(0, min(x_pelota, ANCHO - pelota.get_width()))
    y_pelota = max(0, min(y_pelota, ALTO - pelota.get_height()))

    # Verificar colisiones con pelota
    if (
        x_peppa < x_pelota + pelota.get_width()
        and x_peppa + peppa.get_width() > x_pelota
        and y_peppa < y_pelota + pelota.get_height()
        and y_peppa + peppa.get_height() > y_pelota
    ):
        sonido_fin.play()  # Reproducir sonido de fin de juego
        print("¡Has sido tocado por la burbuja! Juego terminado.")
        pygame.time.delay(5000)  # Esperar 5 segundos antes de reiniciar
        juego_inicial = reiniciar_juego()
        x_peppa, y_peppa = juego_inicial['x_peppa'], juego_inicial['y_peppa']
        velocidad_salto = juego_inicial['velocidad_salto']
        salto_actual = juego_inicial['salto_actual']
        en_suelo = juego_inicial['en_suelo']
        x_pelota, y_pelota = juego_inicial['x_pelota'], juego_inicial['y_pelota']
        velocidad_pelota = juego_inicial['velocidad_pelota']
        x_fondo = juego_inicial['x_fondo']
        tiempo_actual = juego_inicial['tiempo_actual']

    # Dibujar peppa y pelota
    PANTALLA.blit(peppa, (x_peppa, y_peppa))
    PANTALLA.blit(pelota, (x_pelota, y_pelota))

    pygame.display.update()
    reloj.tick(60)
    tiempo_actual += 1

# Juego terminado
print("¡Felicidades! Has sobrevivido el tiempo establecido.")
pygame.quit()
sys.exit()

