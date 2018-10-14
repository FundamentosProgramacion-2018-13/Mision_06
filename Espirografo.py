# Autor: Erick David Ramírez Martínez, A01748155
# Programa que sirve como un espirógrafo

import random
import math
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,L):
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

        K = r / R
        vueltas = r//math.gcd(r,R)

        for angulo in range(0, 360 *vueltas + 1, 1):
            tinte = int(250/360*angulo/vueltas) #Genera un valor entre 0-250 para asignarlo a un color
            color = (255-tinte, tinte, 255) #Genera un degradado de color
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R*((1-K) * math.cos(a) + L*K * math.cos((1-K)/K*a))) #ecuaciones paramétricas
            y = int(R*((1-K) * math.sin(a) - L*K * math.sin((1-K)/K*a)))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí se insertan los valores de r, R y L
def main():

        print("Bienvenido al programa que sirve como un espirógrafo")
        print("")
        r = int(input("Ingrese r el tamaño de los círculos pequeños que crearán el patron: "))
        R = int(input("Ingrese R el tamaño del contorno total que podría ocupar (círculo mayor): "))
        L = float(input("Ingrese L (El cual es un número que determina la separación de los círculos y el patrón, de preferencia inserte un valor muy pequeño entre 0.3 y 3): "))
        dibujar(r,R,L)   # Por ahora, solo dibuja

# Llamas a la función principal
main()