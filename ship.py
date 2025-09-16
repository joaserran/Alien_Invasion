import pygame

class Ship:
    """Una clase para gestionar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y configura su posicion inicial."""
        # ai_game es una referencia a la clase AlienInvasion
        # Asignamos al atributo screen de Ship la pantalla (screen) de 
        # AlienInvasion
        self.screen = ai_game.screen
        # Pygame trata los elementos del juego como rectángulos (rect)
        # El método get_rect() nos devuelve el atributo rect asignado a la
        # pantalla de AlienInvasion
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')
        # Guardamos el atributo rect correspondiente a la nave
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior
        # de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera de movimiento; empieza con una bandera que no se mueve
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave en función de la bandera de 
        movimiento"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        # blit() es un método de pygame que dibuja una imagen sobre otra
        # Aquí lo que hacemos es copiar la imagen de la nave (self.image) y 
        # pegarla en la pantalla (self.screen) en la posición indicada por
        # self.rect
        self.screen.blit(self.image, self.rect)
