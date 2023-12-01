import pygame
import os
import random

# Inicializa Pygame
pygame.init()

# Define tus constantes y carga tus recursos aquí
ANCHO = 800
ALTO = 600
IMAGEN_ANCHO = 100
IMAGEN_ALTO = 100

FONDO_TAMAÑO = (ANCHO, ALTO)
CLIMA_POSICION = (ANCHO // 2, 40)
FONDO = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "imagenes/sol.jpg"))
FONDO = pygame.transform.scale(FONDO, FONDO_TAMAÑO)

# Define la función para cargar imágenes y sonidos
def cargar_recurso(ruta_imagen, ruta_sonido):
    imagen = pygame.transform.scale(pygame.image.load(ruta_imagen), (IMAGEN_ANCHO, IMAGEN_ALTO))
    sonido = pygame.mixer.Sound(ruta_sonido)
    return {"imagen": imagen, "sonido": sonido}

# Carga los recursos
climas = {
    "lluvia": cargar_recurso("imagenes/lluvia.png", "musica/lluvia.wav"),
    "soleado": cargar_recurso("imagenes/sol.png", "musica/sol.wav"),
    "nube": cargar_recurso("imagenes/nube.png", "musica/nube.wav"),
}
fondos = {
    "lluvia": pygame.transform.scale(pygame.image.load("imagenes/lluvia.jpg"), FONDO_TAMAÑO),
    "soleado": pygame.transform.scale(pygame.image.load("imagenes/sol.jpg"), FONDO_TAMAÑO),
    "nube": pygame.transform.scale(pygame.image.load("imagenes/nube.jpg"), FONDO_TAMAÑO),
}

bien_hecho = pygame.image.load("imagenes/bien_hecho.png")
pygame.mixer.music.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "musica/climas.mp3"))
pygame.mixer.music.play(-1)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Coincidir Clima")

clima_actual = random.choice(list(climas.keys()))
fondo_actual = random.choice(list(fondos.keys()))
mostrar_bien_hecho = False
tecla_enter_presionada = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not tecla_enter_presionada:
                clima_actual = random.choice(list(climas.keys()))
                clima_sound = climas[clima_actual]["sonido"]
                clima_sound.play()
                tecla_enter_presionada = True
            elif event.key == pygame.K_SPACE:
                fondo_actual = random.choice(list(fondos.keys()))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                tecla_enter_presionada = False

    pantalla.blit(FONDO, (0, 0))
    pantalla.blit(fondos[fondo_actual], (0, 0))
    pantalla.blit(climas[clima_actual]["imagen"], CLIMA_POSICION)

    if mostrar_bien_hecho:
        pantalla.blit(bien_hecho, (ANCHO // 2 - bien_hecho.get_width() // 2, ALTO // 2 - bien_hecho.get_height() // 2))

    pygame.display.flip()

    if clima_actual == fondo_actual:
        mostrar_bien_hecho = True
    else:
        mostrar_bien_hecho = False

# Detiene la música y cierra Pygame al salir del bucle principal
pygame.mixer.music.stop()
pygame.quit()

