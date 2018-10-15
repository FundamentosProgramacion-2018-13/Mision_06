# encoding: UTF-8
#Autor: María Fernanda Vela Calderón
#Misión imposible: dibujar un espirografo con ecuaciones paramétricas.

import pygame
import random
import math

BLANCO = (255, 255, 255)

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800


def colorAleatorio():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def dibujar(r, R, l):
    periodo = r//math.gcd(r, R)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    k = (r/R)

    pygame.init()
    reloj = pygame.time.Clock()
    termina = False


    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

    for angulo in range(0, 360 * periodo):
        a = math.radians(angulo)
        x = R * ((1-k) * math.cos(angulo) + l * k * math.cos((1-k)/k * (angulo)))
        y = R * ((1-k) * math.sin(angulo) + l * k * math.sin((1-k)/k * (angulo)))
        pygame.draw.circle(ventana, colorAleatorio(), (int(x + ANCHO // 2), int(ALTO // 2 - y)), 1)
        pygame.display.flip()
        reloj.tick(500)
    pygame.quit()


def main():
    r = int ( input("Ingresa el valor de r: "))
    R = int ( input("Ingresa el valor de R: "))
    l = float ( input("Ingresa el valor de l: "))
    dibujar(r, R, l)


main()
