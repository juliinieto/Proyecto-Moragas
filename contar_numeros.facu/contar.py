import sys
import pygame
import random
import os
from pygame.font import Font


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Contar Personas")

hand_images = ["1.png", "2.png", "3.png", "4.png", "5.png"]

person_images = ["persona1.png", "persona2.png", "persona3.png", "persona4.png", "persona5.png"]

ruta_actual = os.path.dirname(os.path.abspath(__file__))
contar = pygame.image.load(os.path.join(ruta_actual, "contar.png"))
contar = pygame.transform.scale(contar, (150, 150))
contar_rect = contar.get_rect(center=(screen_width // 3, 120))

font = Font(None, 36)  

current_hand_index = 0
current_person_index = 0


current_hand = pygame.image.load(hand_images[current_hand_index])
current_person = pygame.image.load(person_images[current_person_index])

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                current_hand_index = (current_hand_index + 1) % len(hand_images)
                current_hand = pygame.image.load(hand_images[current_hand_index])

            elif event.key == pygame.K_SPACE: 
                current_person_index = (current_person_index + 1) % len(person_images)
                current_person = pygame.image.load(person_images[current_person_index])

        background_color = (64, 64, 64)
        screen.fill(background_color)

        instructions_text = "CUENTA CON LAS MANOS"
        text_surface = font.render(instructions_text, True, (255, 255, 255)) 
        screen.blit(text_surface, (250, 20))  

        screen.blit(contar, (350, 40))
        screen.blit(current_person, (150, 200))  
        screen.blit(current_hand, (500, 200))  

        pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()

