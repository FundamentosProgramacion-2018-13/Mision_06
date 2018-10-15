# Autor: Joshua Sánchez Martínez A01274269
# Lee valores para dibujar una figura


import math
import pygame


ANCHO = 800
ALTO = 800


C1 = (255, 255, 255)
C2 = (99, 99, 99)
C3 = (0, 255, 0)
C4 = (255, 0, 0)
C5 = (60, 200, 180)
C6 = (238, 210, 130)
C7 = (0, 0, 0)
C8 = (255, 40, 90)

# Funcion para dibujar
def dibujar(r, R, l):

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(C7)

        for angulo in range(0, 361 * (r//math.gcd(r, R)), 1):
            k = r / R
            x = int(R * ((1.5 - k) * math.cos(angulo) + l * k * math.cos(((1.5- k) / k) * angulo)))
            y = int(R * ((1.5 - k) * math.sin(angulo) - l * k * math.sin(((1.5 - k) / k) * angulo)))
            pygame.draw.circle(ventana, C6,  (x + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, C3, (x + ANCHO//2, ALTO//2 + y), 1)
            pygame.draw.circle(ventana, C5, (x * 2 + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, C1, (x * 2 + ANCHO // 2, ALTO // 2 - 2 * y), 1)
            pygame.draw.circle(ventana, C8, (x * 2 + ANCHO // 2, ALTO // 2 + 2 * y), 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


# Función principal
def main():
    r = 23
    R = 54
    l = 2
    dibujar(r, R, l)


# Llamada a la función principal
main()