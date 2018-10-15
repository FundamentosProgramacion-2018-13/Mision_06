# Autor: Ithan Alexis Pérez Sánchez, A01377717
# Descripción: Mision 6

# El codigo empieza después de esta linea

import math
import random
import pygame

ANCHO = 800
ALTO = 800


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


def dibujar(r, R, L):

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
        ventana.fill(BLANCO)

        Random = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        K = r / R
        Período = r // math.gcd(r, R)

        for angulo in range(0, 360 + 1, 1):  # Primer circulo que se toma como base del proceso
            alfa = math.radians(angulo)
            x1 = int(200 * math.cos(alfa))
            y1 = int(200 * math.sin(alfa))
            pygame.draw.circle(ventana, Random, (x1 + ANCHO // 2, ALTO // 2 - y1), 1, 1)

        for angulo in range(0, 360 * Período, 1):   # Circulo que toma los valores dados desde main
            alfa = math.radians(angulo)
            x1 = int(R * ((1 - K) * math.cos(alfa) + (L * K * math.cos(((1 - K) / K) * alfa))))
            y1 = int(R * ((1 - K) * math.sin(alfa) - (L * K * math.sin(((1 - K) / K) * alfa))))
            pygame.draw.circle(ventana, Random, (x1 + ANCHO // 2, ALTO // 2 - y1), 2)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()  # termina pygame

def main():

    r = int(input("¿Cuántos puntos?: "))
    R = int(input("¿Cuántos puntos?: "))
    L = float(input("¿Cuántos puntos?: "))
    dibujar(r, R, L)
    print("Esto fue lo que pusiste:", r, R, L)

main()