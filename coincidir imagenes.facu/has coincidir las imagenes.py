import pygame
import os
import random

pygame.init()

ANCHO, ALTO = 800, 600
IMAGEN_ANCHO, IMAGEN_ALTO = 150, 150
FONDO_TAMAÑO = (ANCHO, ALTO)
CLIMA_POSICION = (ANCHO // 2, 40)
FONDO = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fondo.jpg"))
FONDO = pygame.transform.scale(FONDO, FONDO_TAMAÑO)

climas = {
    "lluvia": pygame.transform.scale(pygame.image.load("lluvia.png"), (IMAGEN_ANCHO, IMAGEN_ALTO)),
    "soleado": pygame.transform.scale(pygame.image.load("soleado.png"), (IMAGEN_ANCHO, IMAGEN_ALTO)),
    "nieve": pygame.transform.scale(pygame.image.load("nieve.png"), (IMAGEN_ANCHO, IMAGEN_ALTO)),
    "nube": pygame.transform.scale(pygame.image.load("nube.png"), (IMAGEN_ANCHO, IMAGEN_ALTO)),
}

fondos = {
    "lluvia": pygame.transform.scale(pygame.image.load("fondo_lluvia.jpg"), FONDO_TAMAÑO),
    "soleado": pygame.transform.scale(pygame.image.load("fondo_soleado.jpg"), FONDO_TAMAÑO),
    "nieve": pygame.transform.scale(pygame.image.load("fondo_nieve.jpg"), FONDO_TAMAÑO),
    "nube": pygame.transform.scale(pygame.image.load("fondo_nublado.jpg"), FONDO_TAMAÑO),
}

bien_hecho = pygame.image.load("bien_hecho.png")

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Coincidir Clima")

pygame.mixer.music.load("climas.mp3")
pygame.mixer.music.play(-1)

clima_actual = random.choice(list(climas.keys()))
fondo_actual = random.choice(list(fondos.keys()))
mostrar_bien_hecho = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if clima_actual == fondo_actual:
                    mostrar_bien_hecho = True
                else:
                    mostrar_bien_hecho = False  
                clima_actual = random.choice(list(climas.keys()))
            elif event.key == pygame.K_SPACE:
                fondo_actual = random.choice(list(fondos.keys()))

    pantalla.blit(FONDO, (0, 0))

    pantalla.blit(fondos[fondo_actual], (0, 0))

    pantalla.blit(climas[clima_actual], CLIMA_POSICION)

    if mostrar_bien_hecho:
        pantalla.blit(bien_hecho, (ANCHO // 2 - bien_hecho.get_width() // 2, ALTO // 2 - bien_hecho.get_height() // 2))

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()

