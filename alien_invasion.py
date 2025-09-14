# El módulo sys sirve para interactuar con el intérprete.
# Por ejemplo, sys.version muestra la versión de Python
import sys 
# Pygame es una librería externa para crear juegos
import pygame

class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del 
    juego."""

    def __init__(self):
        """Inicializa el juego y crea recursos."""
        # Inicializa todos los módulos importados de pygame
        pygame.init()
        # Controlamos los frames (cuadros por segundo)
        # Vamos a crear un reloj que sonará cada vez que el segundero pase por
        # el bucle principal.
        # Creamos una instancia de la clase Clock contenida en el módulo time
        self.clock = pygame.time.Clock()
        # display es el módulo de pygame para manejar pantallas y ventanas.
        # Inicializa una ventana. El objeto creado se llama Surface (Superficie)
        # Las dimensiones se pasan como una tupla de dos valores
        self.screen = pygame.display.set_mode((1200, 800))
        # Establece el nombre de la ventana
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicializa el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y ratón.
            # La función devuelve como lista los eventos detectados
            for event in pygame.event.get():
                # Si el evento del usuario es pulsar la X de la ventana
                # se sale de python (termina la ejecución)
                if event.type == pygame.QUIT:
                    sys.exit()

            # Hace visible la última pantalla dibujada
            pygame.display.flip()
            # El método tick recibe un argumento: la tasa de frames del juego
            # en milisegundos.
            self.clock.tick(60)

# Este bloque solo se ejecuta si se llama al archivo directamente
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()