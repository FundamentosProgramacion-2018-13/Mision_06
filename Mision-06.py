# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Oh no, ya mamó

# Importar librerías necesarias
import pygame
from math import *


# Colores
blanco = (248, 248, 248)
negro = (38, 38, 38)

# Ajustes iniciales de PyGame
pygame.init()

Ancho = 700
Alto = 700

win = pygame.display.set_mode((Ancho, Alto))

pygame.display.set_caption("Mision 6")

win.fill(negro)


def dibujar(R, r, l, c):
    periodo = r // gcd(r, R)
    l = int((1/l)*40)

    for t in range(0, 360 * periodo):
        if c == 0:
            color = 248, 38, 38
        elif c == 1:
            color = 38, 38, 248
        elif c == 2:
            color = 38, 248, 38
        else:
            color = 248, 248, 248

        x = ((R - r) * cos(r / R * t)) + l * cos((1 - (r / R)) * t)
        y = ((R - r) * sin(r / R * t)) - l * sin((1 - (r / R)) * t)

        pygame.draw.circle(win, color, (int(x + Ancho // 2), int(Alto // 2 - y)), 1)

    pygame.display.update()


def main():
    R = int(input("R: "))
    r = int(input("r: "))
    l = float(input("l: "))
    c = float(input("c: "))
    dibujar(R, r, l, c)


main()

run = True

reloj = pygame.time.Clock()

# Lógica de pygame que básicamente es la función main pero en tiempo real
while run:
    reloj.tick(10)  # Para salvar al planeta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_SPACE]:
            main()
