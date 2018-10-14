# encoding: UTF-8
# Autor: Silvia Ferman Muñoz
# Este programa se dibujaran diferentes figuras utilizando ecuaciones parametricas


# Librerias utilizadas en este programa
import pygame
import random
import math

# Dimensiones pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)


# Función que regresa colores aleatorios
def colorAleatorio():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# En esta función:
# 1. Se calculan "x" y "y" basandose en una ecuacion parametrica
# 2. Se dibuja la mandala con los datos que de el usuario
def dibujarMandalaEspirografo(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        k = r/R

        for angulotheta in range(360 * r // math.gcd(r, R) + 1):

            angulo = math.radians(angulotheta)      # Convierte el angulo a radianes

            x = int(R * ((1 - k) * math.cos(angulo) + l * k * math.cos(((1 - k) / k) * angulo)))
            y = int(R * ((1 - k) * math.sin(angulo) - l * k * math.sin(((1 - k) / k) * angulo)))

            pygame.draw.circle(ventana, colorAleatorio(), ((x + ALTO // 2), (ANCHO // 2 + y)), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


# Función principal
def main():
    r = int(float(input("Inserte el valor de r: ")))
    R = int(float(input("Inserte el valor de R: ")))
    l = float(input("Inserte el valor de l: "))
    dibujarMandalaEspirografo(r, R, l)


# Se llama a la función principal
main()