#Nombre: Alexys Martín Coate Reyes
#Descripción: Crear un diferentes figuras imitando la función de un espirógrafo

import pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)
DESCONOCIDO = (255,35,90)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)


        k = r / R
        periodo = r // math.gcd(r, R)

        for angulo in range(0, 360 * periodo, 1):
             a = math.radians(angulo)
             x = int(R * ((1 - k) * math.cos(a) + (l * k * math.cos(((1 - k) / k) * a))))
             y = int(R * ((1 - k) * math.sin(a) - (l * k * math.sin(((1 - k) / k) * a))))
          #  pygame.draw.circle(ventana,colorAleatorio, (x + ANCHO // 2, ALTO // 2 - y), 1, 1)
             for veces in range(1,5):
                 colorAleatorio = (random.randrange(255), random.randrange(255), random.randrange(255))
                 x2 = veces*x
                 y2 = veces *y
                 pygame.draw.circle(ventana,colorAleatorio, (x2 + ANCHO // 2, ALTO // 2 - y2), 1, 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()

def main():
     r = int(input("Valor de r: "))
     R = int(input("Valor de R: "))
     l = float(input("Valor de l: "))
     dibujar(r, R, l)

main()