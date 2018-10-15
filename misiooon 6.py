# encoding: UTF-8
# Autor de versión usada de pygame (programa base): Roberto Martínez Román
# Programa que sirve para hacer mandalas
# Autor programas Javier Alexandro Vargas Sánchez A01377718

import math
import random
import pygame

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
dodger = (173,216,230)
steel = (70, 130, 180)
midnight = (25, 25, 112)
def leerOpcionMenu():  # Despliega las opciones de actividades al usuario para que escoja una
    print("Misión 5. Seleccione qué quiere hacer")
    print("1. Dibujar mandala ")
    print("2. Dibujar mandala hecho por mi (Javier)")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def dibujarMandalaP():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        r = 65
        R = 220
        l = 0.8

        for angulo in range (0, 361 * (r // math.gcd(r, R)), 1):

            k = r / R

            grados = math.radians(angulo)

            x = int(R * ((1 - k) * math.cos(grados) + l * k * math.cos(((1 - k) / k) * grados)))
            y = int(R * ((1 - k) * math.sin(grados) - l * k * math.sin(((1 - k) / k) * grados)))

            pygame.draw.circle(ventana, ROJO,(x + ANCHO // 2, ALTO // 2 - y), 1)





        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def dibujarMandalaJ():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        r = 500
        R = 150
        l = 0.5

        for angulo in range (0, 361 * (r // math.gcd(r, R)), 1):

            k = r / R

            grados = math.radians(angulo)

            x = int(R * ((1 - k) * math.cos(grados) + l * k * math.cos(((1 - k) / k) * grados)))
            y = int(R * ((1 - k) * math.sin(grados) - l * k * math.sin(((1 - k) / k) * grados)))

            pygame.draw.circle(ventana, steel, (x // 4 + ANCHO // 2, ALTO // 2 - y // 4), 1)
            pygame.draw.circle(ventana, midnight, (x // 2 + ANCHO // 2, ALTO // 2 - y // 2), 1)
            pygame.draw.circle(ventana, dodger, (x // 16 + ANCHO // 2, ALTO // 2 - y // 16), 1)






        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def main():
    opcion = leerOpcionMenu()
    if opcion == 1:
        dibujarMandalaP()
    elif opcion == 2:
        dibujarMandalaJ()
    elif opcion == 0:
        print("Termina programa.")
    else:
        print("Teclea opciones válidas")

main()
