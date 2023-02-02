import sys, pygame


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((480, 240))

    def bucle_principal(self):
        while True:
            pygame.draw.rect(
                self.pantalla, (255, 232, 2), 
                pygame.Rect(0, 0, 100, 50))
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()