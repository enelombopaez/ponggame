import sys, pygame

ANCHO = 640
ALTO = 480
COLOR_BLANCO = (255, 232, 2) #amarillo

ANCHO_PALETA = 10
ALTO_PALETA = 40

MARGEN_LATERAL = 40

class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
            pygame.draw.rect(
                self.pantalla, (COLOR_BLANCO), 
                pygame.Rect(
                    MARGEN_LATERAL, 
                    (ALTO-ALTO_PALETA)/2 , 
                    ANCHO_PALETA, 
                    ALTO_PALETA))
            
            pygame.draw.rect(
                self.pantalla, (COLOR_BLANCO), 
                pygame.Rect(
                    ANCHO - MARGEN_LATERAL - ANCHO_PALETA, 
                    (ALTO-ALTO_PALETA)/2 , 
                    ANCHO_PALETA, 
                    ALTO_PALETA))            
        
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()