import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creación de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adivina el animal")

# Cargar sonidos y nombres de animales
animal_data = [
    {"name": "perro", "sound": pygame.mixer.Sound("perro.wav")},
    {"name": "gato", "sound": pygame.mixer.Sound("gato.wav")},
    {"name": "elefante", "sound": pygame.mixer.Sound("elefante.wav")},
]

# Cargar imágenes de animales
animal_images = [
    pygame.image.load("perro.png"),
    pygame.image.load("gato.png"),
    pygame.image.load("elefante.png"),
    # Agrega aquí las imágenes de los otros animales
]

current_animal = None

# Cargar una fuente para mostrar instrucciones y mensajes
font = pygame.font.Font(None, 36)

def load_random_animal():
    global current_animal
    current_animal = random.choice(animal_data)

def main():
    load_random_animal()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_animal["sound"].play()
                if event.key == pygame.K_r:
                    load_random_animal()

        screen.fill(BLACK)
        instructions = font.render("Presiona ESPACIO para escuchar el sonido. Presiona R para otro sonido.", True, WHITE)
        screen.blit(instructions, (50, 50))

        # Dibuja las imágenes de los animales en la parte superior
        for i in range(4):
            screen.blit(animal_images[i], (i * 200, 100))

        # Dibuja las imágenes de los animales en la parte inferior
        for i in range(4):
            screen.blit(animal_images[i + 4], (i * 200, 300))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
