

import pygame

ANCHO = 800
ALTO = 600

C_BLANCO = (255, 255, 255)

ANCHO_PALETA = 10
ALTO_PALETA = 40
MARGEN_LATERAL = 40

TAM_PELOTA = 5

"""
Reto 1: Pintar la red
Reto 2: Cambiar el color del campo y los elementos
Reto 3: Salir del juego pulsando la tecla ESC
¡IMPORTANTE! https://www.pygame.org/docs/
"""


class Jugador(pygame.Rect):
    def __init__(self, pos_x, pos_y):
        self.rectangulo = pygame.Rect(pos_x, pos_y, ANCHO_PALETA, ALTO_PALETA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_BLANCO, self.rectangulo)


class Pelota(pygame.Rect):
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(x, y, TAM_PELOTA, TAM_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_BLANCO, self.rectangulo)


class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

        pos_y = (ALTO-ALTO_PALETA)/2
        pos_x_2 = ANCHO-MARGEN_LATERAL-ANCHO_PALETA
        self.jugador1 = Jugador(MARGEN_LATERAL, pos_y)
        self.jugador2 = Jugador(pos_x_2, pos_y)

        pelota_x = (ANCHO-TAM_PELOTA)/2
        pelota_y = (ALTO-TAM_PELOTA)/2
        self.pelota = Pelota(pelota_x, pelota_y)

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)
            self.pelota.pintame(self.pantalla)
            pygame.display.flip()


if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()