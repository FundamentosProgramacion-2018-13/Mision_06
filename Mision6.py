# Author: Ivan Honc Ayón
# Descripción: Este programa hace un espirógrado.

import math
import random

import pygame


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)


# Esta función convierte los valores y los sustituye en operaciones algebraicas para formar distintas
# figuras.
def dibujarPuntosCirculo(ventana, r, R, l):
    radio = 100
    k =r/R
    for x in range(0, 360 * r//math.gcd(r, R)):
        color1 = (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))

        alfa = math.radians(x)
        x1 = int(R*(((l-k)*math.cos(alfa))+(l*k*(math.cos(((l-k)*(alfa))/k)))))
        y1 = int(R*(((l-k)*math.sin(alfa))+(l*k*(math.sin(((l-k)*(alfa))/k)))))
        pygame.draw.circle(ventana, color1, (x1+ANCHO//2, ALTO//2-y1), 1)


# Esta función inicia pygame y sus funciones, asimismo manda a llamar a las funciones que
# requieren de pygame.
def dibujarFiguras(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarPuntosCirculo(ventana, r, R, l)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# Esta función pide los valores requeridos, se asegura de que sean válidos y manda llamar a
# las tras funciones.
def main():
    r = int(input("Ingresa el valor de r: "))
    R = int(input("Ingresa el valor de R: "))
    l = int(input("Ingresa el valor de l: "))
    while r==0 or R==0 or l ==0 or l>=10:
        print("Valores incorrectos, escríbalos de nuevo: ")
        r = int(input("Ingresa el valor de r: "))
        R = int(input("Ingresa el valor de R: "))
        l = int(input("Ingresa el valor de l: "))
    dibujarFiguras(r, R, l)


main()
