import pygame
import math
import random

ANCHO = 800
ALTO = 800

azuloscuro = (1, 41, 97)
magenta = (171, 46, 129)
rosaoscuro = (125, 52, 130)
rosaclaro = (209, 125, 195)


def dibujar():

    radioExterno = 314
    radioInterno = 31
    l = 1.415926
    k = radioInterno / radioExterno
    periodo = radioInterno//math.gcd(radioInterno, radioExterno)

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(azuloscuro)

        for angulo in range(0, (360*periodo)+1):
            c = random.randint(0, 20)
            if 0 <= c <= 9:
                color = magenta
            if 10 <= c <= 12:
                color = rosaclaro
            if 13 <= c <= 20:
                color = rosaoscuro
            a = math.radians(angulo)
            x = int(radioExterno*((1-k)*math.cos(a)+l*k*(math.cos((1-k)*a/k))))
            y = int(radioExterno*((1-k)*math.sin(a)-l*k*(math.sin((1-k)*a/k))))
            pygame.draw.circle(ventana, color, (ANCHO//2 + x, ALTO//2 - y), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    dibujar()


main()
