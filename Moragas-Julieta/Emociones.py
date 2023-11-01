import pygame

# Inicializa pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("EMOCIONES")

# Carga una lista de imágenes
imagenes = ["img/alegría.png", "img/enfado.png", "img/tristeza.png"]  # Reemplaza con las rutas de tus imágenes
imagen_actual = 0

# Lista de rutas de archivos WAV correspondientes a cada imagen
sonidos_wav = ["sonido/feliz.wav", "sonido/enfado.wav", "sonido/triste.wav"]  # Reemplaza con las rutas correctas

# Configuración de fuente para el texto
fuente = pygame.font.Font(None, 36)
fuente_texto = pygame.font.Font(None, 36)  # Aumenta el tamaño de fuente
texto_superior = fuente.render("¿CÓMO TE SIENTES HOY?", True, (0, 0, 0))
textos = ["FELIZ", "ENOJADO", "TRISTE"]

# Lista de colores de fondo que coinciden con las imágenes
colores_fondo = [(255, 255, 0), (255, 0, 0), (0, 0, 255)]

# Carga el archivo de sonido WAV correspondiente a la primera imagen
pygame.mixer.init()
pygame.mixer.music.load(sonidos_wav[imagen_actual])  # Carga el sonido correspondiente

# Bucle principal
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            # Cuando se presiona la tecla "Enter", avanza a la siguiente imagen
            imagen_actual = (imagen_actual + 1) % len(imagenes)
            pygame.mixer.music.load(sonidos_wav[imagen_actual])  # Carga el sonido correspondiente
            pygame.mixer.music.play()  # Reproduce el sonido
            
    
  # Establece el color de fondo de acuerdo con la imagen actual
    ventana.fill(colores_fondo[imagen_actual])

    # Dibuja la imagen en la ventana
    imagen = pygame.image.load(imagenes[imagen_actual])
    ventana.blit(imagen, (ventana_ancho // 2 - imagen.get_width() // 2, ventana_alto // 2 - imagen.get_height() // 2))

    # Dibuja el texto en la parte superior de la ventana
    texto_superior = fuente.render("¿CÓMO TE SIENTES HOY?", True, (0, 0, 0))
    ventana.blit(texto_superior, (ventana_ancho // 2 - texto_superior.get_width() // 2, 10))

    # Dibuja el texto en la parte inferior de la ventana
    texto_inferior = fuente_texto.render(textos[imagen_actual], True, (0, 0, 0))
    ventana.blit(texto_inferior, (ventana_ancho // 2 - texto_inferior.get_width() // 2, ventana_alto - 50))

    # Actualiza la ventana
    pygame.display.update()

# Cierra pygame
pygame.quit()
