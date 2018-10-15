# Autor :  Humberto Carrillo Gómez
# Este programa utiliza pygame para producir un diseño parecido a los que se pueden realizar con un espirógrafo.

import math     # Librería de matemáticas
import pygame   # Librería de pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
greenYellow = (173, 255, 47)
violet = (238, 130, 228)                # Colores extra
negro = (0, 0, 0)
cyan = (0, 255, 255)
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
        ventana.fill(negro)
        #colorRandom = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        for angulo in range(0, 361 * (r//math.gcd(r, R)), 1):
            k = r / R
            x = int(R * ((1 - k) * math.cos(angulo) + l * k * math.cos(((1 - k) / k) * angulo)))
            y = int(R * ((1 - k) * math.sin(angulo) - l * k * math.sin(((1 - k) / k) * angulo)))
            pygame.draw.circle(ventana, violet,  (x + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 + y), 1)
            pygame.draw.circle(ventana, greenYellow, (x * 2 + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, BLANCO, (x * 2 + ANCHO // 2, ALTO // 2 - 2 * y), 1)
            pygame.draw.circle(ventana, cyan, (x * 2 + ANCHO // 2, ALTO // 2 + 2 * y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = 90
    R = 220
    l = 0.8
    dibujar(r, R, l)


# Llamada a la función principal
main()