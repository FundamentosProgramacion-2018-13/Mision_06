# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Hacer un espirógrafo


# Importar librerías necesarias
import pygame
import random
from math import *

def dibujar(r, R, l):
    # Colores
    blanco = (248, 248, 248)
    negro = (38, 38, 38)

    # Ajustes iniciales de PyGame
    pygame.init()

    Ancho = 800
    Alto = 800

    win = pygame.display.set_mode((Ancho, Alto))

    pygame.display.set_caption("Mision 6")

    win.fill(blanco)

    k = r/R
    periodo = int(r // (r*R))

    for angulo in range(0, periodo, 1):
        a = radians(angulo)
        x = R*(l-k)*cos(a)+(l*k*cos((l-k)*cos(a)/k))
        y = R*(l-k)*sin(a)-(l*k*sin((l-k)*a/k))
        pygame.draw.circle(win, negro, (int(x+Ancho//2), int(Alto//2-y)), int(r), 1)

    pygame.display.update()

    run = True

    reloj = pygame.time.Clock()

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


def main():
    r = float(input("r: "))
    R = float(input("R: "))
    l = float(input("l: "))
    dibujar(r, R, l)


main()
