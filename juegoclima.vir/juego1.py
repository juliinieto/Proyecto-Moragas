import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Imágenes y Sonidos")

# Tamaño deseado para todas las imágenes
image_width, image_height = 800, 600

# Lista de imágenes
images = [r'C:\Users\Belen\OneDrive\Documentos\juego1\img\nublado.jpg', r'C:\Users\Belen\OneDrive\Documentos\juego1\img\soleado.jpg', r'C:\Users\Belen\OneDrive\Documentos\juego1\img\lluvioso.jpg']
current_image_index = 0

# Lista de sonidos
sounds = [r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\nublado.wav', r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\soleado.wav', r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\lluvioso.wav']
current_sound_index = 0

# Cargar y redimensionar la primera imagen
current_image = pygame.image.load(images[current_image_index])
current_image = pygame.transform.scale(current_image, (image_width, image_height))

# Función para cargar y reproducir el siguiente sonido
def next_sound():
    global current_sound_index
    current_sound_index = (current_sound_index + 1) % len(sounds)
    pygame.mixer.music.load(sounds[current_sound_index])
    pygame.mixer.music.play()

# Función para cargar y reproducir el sonido personalizado "muy bien"
def play_muybien_sound():
    muybien_sound = pygame.mixer.Sound(r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\muybien.wav')
    muybien_sound.play()

# Función para cargar y reproducir el sonido personalizado "muybiensoleado"
def play_muybiensoleado_sound():
    muybiensoleado_sound = pygame.mixer.Sound(r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\muybiensoleado.wav')
    muybiensoleado_sound.play()
    
def play_muybienlluvioso_sound():
    muybienlluvioso_sound = pygame.mixer.Sound(r'C:\Users\Belen\OneDrive\Documentos\juego1\sonido\muybienlluvioso.wav')
    muybienlluvioso_sound.play()

# Definir la función para avanzar a la siguiente imagen
def next_image():
    global current_image_index, current_image
    current_image_index = (current_image_index + 1) % len(images)
    # Cargar y redimensionar la siguiente imagen
    next_image = pygame.image.load(images[current_image_index])
    current_image = pygame.transform.scale(next_image, (image_width, image_height))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_sound()  # Cargar y reproducir el siguiente sonido
                next_image()  # Avanzar a la siguiente imagen
            elif event.key == pygame.K_RETURN:
                if current_image_index == 0:
                    play_muybien_sound()  # Reproducir "muy bien" cuando se muestra la imagen 1 y se presiona Enter
                elif current_image_index == 1:
                    play_muybiensoleado_sound()  # Reproducir "muybiensoleado" cuando se muestra la imagen 2 y se presiona Enter
                elif current_image_index == 2:
                    play_muybienlluvioso_sound()
    screen.fill((255, 255, 255))
    screen.blit(current_image, (0, 0))
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
sys.exit()
