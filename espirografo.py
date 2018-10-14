# Autor: Mariana Caballero Cabrera
# Dibujar una mandala con medidas que proporciona el usuario

import pygame   # Librería de pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (38,38,38)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Función para hacer los colores random
def colorAleatorio():

    return random.randint(0,255),random.randint(0,255),random.randint(0,255)


# funcion que va a dibujar la mandala
def dibujarmandala (ventana,r,R,l):

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        k = (r / R)
        vueltasperiodo = r // math.gcd(r, R) * 360


        for angulo in range(0, vueltasperiodo + 1, 1):

            anguloValorRadianes = math.radians(angulo)
            x = int (R*((1 - k) * (math.cos(anguloValorRadianes)) + l * k * (math.cos(((1 - k) / k) * anguloValorRadianes)))) #ecuación principal en x
            y = int (R*((1 - k) * (math.sin(anguloValorRadianes)) + l * k * (math.sin(((1 - k) / k) * anguloValorRadianes)))) #ecuacion principal en y
            pygame.draw.circle(ventana, VERDE_BANDERA, (x + ANCHO // 2, ALTO // 2 - y), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    ventana = pygame.display.set_mode((ANCHO, ALTO))

    r = int(input("Teclea r: "))
    R = int (input("Teclea R: "))
    l = float(input("Teclea l: "))

    dibujarmandala(ventana,r,R,l)

#LLamamos a la función principal
main()