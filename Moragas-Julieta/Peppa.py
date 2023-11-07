import pygame
import random

# Inicializa pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("PEPPA PIG")

# Carga una lista de imágenes
imagen = "img/peppapig.png"  # Coloca la ruta de la imagen que desees mostrar
imagen = pygame.image.load(imagen)

# Redimensiona la imagen para hacerla más pequeña
nuevo_ancho = 100  # Ancho deseado
nuevo_alto = 100  # Alto deseado
imagen = pygame.transform.scale(imagen, (nuevo_ancho, nuevo_alto))

# Configuración de fuente para el texto
fuente = pygame.font.Font(None, 36)

# Contador de nivel
nivel = 1

# Función para avanzar al siguiente nivel
def siguiente_nivel():
    global nivel
    nivel += 1

def main():
    ejecutando = True

    while ejecutando:
        cantidad_imagenes_nivel = random.randint(1, 5)  # Número aleatorio de veces que se mostrará la imagen en el nivel
        contador_enter = 0  # Contador de veces que se ha presionado Enter en este nivel

        while contador_enter < cantidad_imagenes_nivel:
            ventana.fill((255, 255, 255))

            # Muestra la imagen en el centro de la ventana
            for i in range(cantidad_imagenes_nivel):
                x = (ventana_ancho // 2) - (imagen.get_width() * cantidad_imagenes_nivel / 2) + i * imagen.get_width()
                y = ventana_alto // 2 - imagen.get_height() // 2
                ventana.blit(imagen, (x, y))

            # Muestra el contador en la esquina superior izquierda
            texto_contador = fuente.render(f"Presiona Enter {contador_enter}/{cantidad_imagenes_nivel} veces", True, (0, 0, 0))
            ventana.blit(texto_contador, (10, 10))

            # Muestra el nivel en la esquina superior derecha
            texto_nivel = fuente.render(f"Nivel {nivel}", True, (0, 0, 0))
            ventana.blit(texto_nivel, (ventana_ancho - texto_nivel.get_width() - 10, 10))

            pygame.display.update()

            # Espera a que el jugador presione Enter
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    contador_enter += 1

        # El jugador ha presionado Enter la cantidad correcta de veces, pasa al siguiente nivel
        siguiente_nivel()

    # Cierra pygame
    pygame.quit()

if __name__ == "__main__":
    main()

