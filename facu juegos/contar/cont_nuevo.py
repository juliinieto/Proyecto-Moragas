import sys
import pygame
import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Contar Personas")

hand_images = ["img/1.png", "img/2.png", "img/3.png", "img/4.png", "img/5.png"]

person_images = ["img/persona1.png", "img/persona2.png", "img/persona3.png", "img/persona4.png", "img/persona5.png"]

current_hand_index = 0
current_person_index = 0

current_hand = pygame.image.load(hand_images[current_hand_index])
current_person = pygame.image.load(person_images[current_person_index])

# Cargar sonidos
sounds = [pygame.mixer.Sound(f"sonido/{i}.wav") for i in range(1, 6)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Reproducir sonido correspondiente al índice actual
                sounds[current_hand_index].play()
                current_hand_index = (current_hand_index + 1) % len(hand_images)
                current_hand = pygame.image.load(hand_images[current_hand_index])

            elif event.key == pygame.K_SPACE:
                current_person_index = (current_person_index + 1) % len(person_images)
                current_person = pygame.image.load(person_images[current_person_index])

    background_color = (64, 64, 64)
    screen.fill(background_color)

    screen.blit(current_person, (250, 50))
    screen.blit(current_hand, (280, 320))

    pygame.display.flip()

pygame.quit()
sys.exit()

