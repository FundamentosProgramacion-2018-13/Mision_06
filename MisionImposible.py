# encoding: UTF-8
# Autor: David Isaí López Jaimes
# Muestar la figura de un espirógrafo

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0 , 0)

def colorRandom():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
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

        for n in range(100):
            x = int(110 * math.cos(math.radians(-3.6 * (n + 1))))
            y = int(110 * math.sin(math.radians(-3.6 * (n + 1))))
            pygame.draw.circle(ventana, colorRandom(), (ANCHO // 2 + x, ANCHO // 2 + y), 75, 1)
        for n in range(30):
            x = int(55 * math.cos(math.radians(-12 * (n + 1))))
            y = int(55 * math.sin(math.radians(-12 * (n + 1))))
            pygame.draw.circle(ventana, colorRandom(), (ANCHO // 2 + x, ANCHO // 2 + y), 75, 1)






        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()