import pygame
import sys
import os

# Inicializa Pygame
pygame.init()

# Configura la pantalla del primer juego
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego")

# Define una estructura de datos que asocie imágenes con sus sonidos correspondientes
image_sound_mapping = {
    'jugar.jpg': 'jugar.wav',
    'merendar.jpg': 'merendar.wav',
    'abajo.jpg': 'pasarabajo.wav',
    'pasar.jpg': 'pasararriba.wav',
    'saludo.jpg': 'saludar.wav',
    'bandera.jpg': 'bandera.wav',
    'cantar.jpg': 'cantar.wav',
    'salir.jpg': 'salir.wav',
    'casa.jpg': 'casa.wav',
    'recreo.jpg': 'recreo.wav'
}

# Define el orden de las imágenes en el primer juego
image_order = [
    'bandera.jpg',
    'cantar.jpg',
    'saludo.jpg',
    'salir.jpg',
    'jugar.jpg',
    'abajo.jpg',
    'pasar.jpg',
    'recreo.jpg',
    'merendar.jpg',
    'casa.jpg'
]

# Crea una lista para almacenar tus imágenes y sonidos en el orden especificado
image_directory = r'C:\Users\virni\Documents\actividades.vir\img'
sound_directory = r'C:\Users\virni\Documents\actividades.vir\sonidos'

image_names = [image_name for image_name in image_order]
sound_names = [image_sound_mapping.get(image_name) for image_name in image_names]

# Carga todas las imágenes
images = [pygame.image.load(os.path.join(image_directory, image_name)) for image_name in image_names]

# Define el tamaño deseado para todas las imágenes
desired_image_size = (700, 600)  # Cambia estos valores según el tamaño que desees

# Redimensiona todas las imágenes al tamaño deseado
images = [pygame.transform.scale(image, desired_image_size) for image in images]

# Carga los sonidos
sounds = [pygame.mixer.Sound(os.path.join(sound_directory, sound_name)) if sound_name is not None else None for sound_name in sound_names]
# Establece variables para el bucle del juego
running = True
image_index = 0

# Inicializa el reproductor de sonido de Pygame
pygame.mixer.init()

# Asigna el sonido "terminar.wav" desde el directorio de sonidos
terminar_sound = pygame.mixer.Sound(os.path.join(sound_directory, 'terminar.wav'))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Si se hace clic con el botón izquierdo del mouse, avanza al siguiente índice de imagen
            if event.button == 1:
                image_index = (image_index + 1) % len(images)
                # Reproduce el sonido correspondiente al cambiar de imagen
                current_sound = sounds[image_index]
                if current_sound:
                    current_sound.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Reproduce el sonido "terminar.wav" al presionar Espacio
                terminar_sound.play()
            elif event.key == pygame.K_RETURN:
                # Avanza al siguiente índice de imagen al presionar Enter
                image_index = (image_index + 1) % len(images)
                # Reproduce el sonido correspondiente al cambiar de imagen
                current_sound = sounds[image_index]
                if current_sound:
                    current_sound.play()

    # Limpia la pantalla
    screen.fill((255, 255, 255))

    # Dibuja la imagen actual en la pantalla
    current_image = images[image_index]
    screen.blit(current_image, (0, 0))

    # Actualiza la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
sys.exit()
