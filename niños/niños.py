import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Imágenes")

# Lista de rutas de imágenes
image_paths = [r"C:\Users\virni\Documents\niños\img\lara.jpg",
               r"C:\Users\virni\Documents\niños\img\camila.jpg",
               r"C:\Users\virni\Documents\niños\img\zayn.jpg",
               r"C:\Users\virni\Documents\niños\img\ambar.jpg"]

# Cargar las imágenes
images = [pygame.image.load(path) for path in image_paths]

# Aumentar el tamaño de las imágenes con suavizado
desired_image_size = (700, 600)
images = [pygame.transform.smoothscale(image, desired_image_size) for image in images]

# Lista de listas de rutas de sonido
sound_paths_list = [
    [r"C:\Users\virni\Documents\niños\sonidos\laa.wav", r"C:\Users\virni\Documents\niños\sonidos\ra.wav", r"C:\Users\virni\Documents\niños\sonidos\lara.wav"],
    [r"C:\Users\virni\Documents\niños\sonidos\ca.wav", r"C:\Users\virni\Documents\niños\sonidos\mi.wav", r"C:\Users\virni\Documents\niños\sonidos\la.wav", r"C:\Users\virni\Documents\niños\sonidos\camila.wav"],
    [r"C:\Users\virni\Documents\niños\sonidos\za.wav", r"C:\Users\virni\Documents\niños\sonidos\yn.wav", r"C:\Users\virni\Documents\niños\sonidos\zayn.wav"],
    [r"C:\Users\virni\Documents\niños\sonidos\am.wav", r"C:\Users\virni\Documents\niños\sonidos\bar.wav", r"C:\Users\virni\Documents\niños\sonidos\ambar.wav"]
]

# Cargar los sonidos
sounds_list = [[pygame.mixer.Sound(path) for path in sound_paths] for sound_paths in sound_paths_list]

# Configuración inicial
current_index = 0
current_sound_index = 0
image_speed = 5

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variable para manejar el evento personalizado
PLAY_SOUND_EVENT = pygame.USEREVENT + 1

# Función para mostrar la imagen actual
def show_image(index):
    screen.blit(images[index], ((screen_width - desired_image_size[0]) // 2, (screen_height - desired_image_size[1]) // 2))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(images)
                current_sound_index = 0  # Reiniciar el índice de sonido al cambiar de imagen
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1 + len(images)) % len(images)
                current_sound_index = 0  # Reiniciar el índice de sonido al cambiar de imagen
            elif event.key == pygame.K_RETURN:  # Tecla Enter
                # Enviar un evento personalizado para reproducir el sonido
                pygame.event.post(pygame.event.Event(PLAY_SOUND_EVENT))

    # Manejar el evento personalizado para reproducir el sonido
    for event in pygame.event.get():
        if event.type == PLAY_SOUND_EVENT:
            current_sound = sounds_list[current_index % len(sounds_list)][current_sound_index % 4]
            current_sound.play()
            print(f"Reproduciendo sonido {current_sound_index + 1} para imagen {current_index + 1}")
            current_sound_index += 1

    # Dibujar la imagen actual en la pantalla
    screen.fill((255, 255, 255))  # Llenar la pantalla con blanco (puedes ajustar el color)
    show_image(current_index)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    clock.tick(image_speed)
