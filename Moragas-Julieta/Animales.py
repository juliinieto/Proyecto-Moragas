import pygame

# Inicializa pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Animales")

# Carga una lista de imágenes
imagenes = ["img/vaca.png", "img/oveja.png", "img/gallina.png"]  # Reemplaza con las rutas de tus imágenes
imagen_actual = 0

# Carga una lista de sonidos
sonidos_wav = ["sonido/vaca.wav", "sonido/oveja.wav", "sonido/gallina.wav"]

# Carga una lista de textos
textos = ["VACA", "OVEJA", "GALLINA"]

# Configuración de fuente para el texto del botón "Siguiente"
fuente_boton = pygame.font.Font(None, 36)

# Configuración de fuente para el texto debajo de la imagen
fuente_texto = pygame.font.Font(None, 90)

# Carga el archivo de sonido WAV correspondiente a la primera imagen
pygame.mixer.init()
pygame.mixer.music.load(sonidos_wav[imagen_actual])  # Carga el sonido correspondiente

# Función para avanzar a la siguiente imagen
def siguiente_imagen():
    global imagen_actual
    imagen_actual = (imagen_actual + 1) % len(imagenes)

# Bucle principal
ejecutando = True
mostrar_texto = False

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            # Cuando se presiona la tecla "Enter", muestra el texto y reproduce el sonido
            mostrar_texto = True
            pygame.mixer.music.load(sonidos_wav[imagen_actual])  # Carga el sonido correspondiente
            pygame.mixer.music.play()  # Reproduce el sonido
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x > ventana_ancho - 100 and y < 100:
                # Cuando se hace clic en el botón "Siguiente", cambia de imagen
                siguiente_imagen()
                mostrar_texto = False

    # Dibuja la imagen en la ventana
    ventana.fill((255, 255, 255))
    imagen = pygame.image.load(imagenes[imagen_actual])
    ventana.blit(imagen, (ventana_ancho // 2 - imagen.get_width() // 2, ventana_alto // 2 - imagen.get_height() // 2))

    # Dibuja el botón "Siguiente" en la esquina superior derecha
    pygame.draw.rect(ventana, (0, 128, 255), (ventana_ancho - 125, 0, 125, 50))
    texto_siguiente = fuente_boton.render("Siguiente", True, (0, 0, 0))
    ventana.blit(texto_siguiente, (ventana_ancho - 120, 10))

    # Dibuja el texto si está definido y la bandera mostrar_texto es True
    if mostrar_texto:
        texto = fuente_texto.render(textos[imagen_actual], True, (0, 0, 0))
        ventana.blit(texto, (ventana_ancho // 2 - texto.get_width() // 2, ventana_alto // 2 + imagen.get_height() // 2))

    # Actualiza la ventana
    pygame.display.update()

# Cierra pygame
pygame.quit()
