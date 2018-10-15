# encoding: UTF-8
# Autor: Irma Gómez Carmona
# Generar figuras mediante la simulación de un pirógrafo

import pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 700
ALTO = 700
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

#color aleatorios para la figuras
color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def dibujarFiguras(r, R, l, ventana):

    K=r/R
    numVueltas=r//math.gcd(r,R) #numero de vueltas para completar un periodo

    for angulo in range (0, 360*numVueltas+1,1):
        if angulo>360*(numVueltas//2): #para la mitad del dibujo será un color para la otra mitad otro
         color=color1
        else:
            color=color2
        anguloRadianes= math.radians(angulo) #convierte los grados en radianes
        x= int(R* ((1-K) * math.cos(anguloRadianes) + l * K * math.cos((1 - K) / K * anguloRadianes))) #posición en x de P
        y = int(R * ((1 - K) * math.sin(anguloRadianes) - l * K * math.sin((1 - K) / K * anguloRadianes))) #posición en y de P
        pygame.draw.circle(ventana,color,(x+ANCHO//2,ALTO//2-y),1,1) #dibuja las curvas


def dibujar(r,R,l):
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


        dibujarFiguras(r,R,l, ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#recibe valores del usuario para r, R y l
def main():
    r= int(input("Valor de r: "))
    R = int(input("Valor de R: "))
    l= float(input("Valor de l: "))
    dibujar(r,R,l)


# Llamas a la función principal
main()