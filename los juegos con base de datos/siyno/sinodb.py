import pygame
import sys
import sqlite3

def cargar_imagen_y_sonido(nombre, tipo, cursor):
    cursor.execute('SELECT ruta FROM elementos WHERE nombre = ? AND tipo = ?', (nombre, tipo))
    resultado = cursor.fetchone()
    if resultado:
        ruta = resultado[0]
        if tipo == 'imagen':
            imagen = pygame.image.load(ruta)
            return imagen
        elif tipo == 'sonido':
            sonido = pygame.mixer.Sound(ruta)
            return sonido
    return None

def main():
    pygame.init()

    pantalla = pygame.display.set_mode((419, 418))
    pygame.display.set_caption("Juego Sí o No")

    fondo = pygame.Surface(pantalla.get_size())
    fondo.fill((255, 255, 255))  # Rellena el fondo con blanco

    conn = sqlite3.connect('elementos.db')  # Reemplaza 'tu_base_de_datos.db' con el nombre de tu base de datos
    cursor = conn.cursor()

    fuente = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    pantalla.blit(fondo, (0, 0))  # Rellena la pantalla con el fondo blanco
                    imagen = cargar_imagen_y_sonido("si", "imagen", cursor)
                    if imagen:
                        pantalla.blit(imagen, (0, 0))
                        pygame.display.flip()
                        sonido = cargar_imagen_y_sonido("si", "sonido", cursor)
                        if sonido:
                            sonido.play()
                elif evento.key == pygame.K_SPACE:
                    pantalla.blit(fondo, (0, 0))  # Rellena la pantalla con el fondo blanco
                    imagen = cargar_imagen_y_sonido("no", "imagen", cursor)
                    if imagen:
                        pantalla.blit(imagen, (0, 0))
                        pygame.display.flip()
                        sonido = cargar_imagen_y_sonido("no", "sonido", cursor)
                        if sonido:
                            sonido.play()

        pygame.display.flip()
        clock.tick(30)  # Limita la velocidad de actualización

if __name__ == "__main__":
    main()
