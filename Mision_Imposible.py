# Luis Ricardo Chagala Cervantes
# Programa que dibuja espirógrafo a trevez de circulos.

import pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)


        k = r/R
        periodo = r//math.gcd(r, R)

        #color
        coloraleatorio = (random.randrange(255), random.randrange(255), random.randrange(255))
        coloraleatorio2 = (random.randrange(255), random.randrange(255), random.randrange(255))
        coloraleatorio3 = (random.randrange(255), random.randrange(255), random.randrange(255))
        coloraleatorio4 = (random.randrange(255), random.randrange(255), random.randrange(255))

        #circulos
        u = r * 2
        U = R * 2
        o = l * 2
        p = u / U

        f = r * 3
        F = R * 3
        h = l * 3
        j = f / F

        z = r * 4
        Z = R * 4
        v = l * 4
        b = z / Z

        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-k) * math.cos(a) + (l * k * math.cos(((1-k)/k)*a))))
            y = int(R * ((1-k) * math.sin(a) - (l * k * math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, coloraleatorio, (x + ANCHO//2, ALTO//2 - y), 1, 1)
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-p) * math.cos(a) + (o * p * math.cos(((1-p)/p)*a))))
            y = int(R * ((1-p) * math.sin(a) - (o * p * math.sin(((1-p)/p)*a))))
            pygame.draw.circle(ventana, coloraleatorio2, (x + ANCHO//2, ALTO//2 - y), 1, 1)
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-j) * math.cos(a) + (h * j * math.cos(((1-j)/j)*a))))
            y = int(R * ((1-j) * math.sin(a) - (h * j * math.sin(((1-j)/j)*a))))
            pygame.draw.circle(ventana, coloraleatorio3, (x + ANCHO//2, ALTO//2 - y), 1, 1)
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-b) * math.cos(a) + (v * b * math.cos(((1-b)/b)*a))))
            y = int(R * ((1-b) * math.sin(a) - (v * b * math.sin(((1-b)/b)*a))))
            pygame.draw.circle(ventana, coloraleatorio4, (x + ANCHO//2, ALTO//2 - y), 1, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)

    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Valor de r: "))
    R = int(input("Valor de R: "))
    l = float(input("Valor de l: "))
    dibujar(r, R, l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()