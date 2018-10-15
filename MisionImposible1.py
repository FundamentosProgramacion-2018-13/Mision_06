#Autor: Víctor Manuel Rodríguez Loyola
#Dibuja círculos usando ecuaciones paramétricas.
import pygame
import math
import random


ALTO= 800
ANCHO=800

BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
NARANJA= (255,128,0)


def dibujarConEspirografo(r,R,l): #Dibuja en una ventana de Pygame diferentes figuras a base de círculos utilizando ecuaciones paramétricas.
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        periodoInterno = r // math.gcd(r, R)
        k = r / R
        for angulo in range(0, 360*periodoInterno+1, 1):
            theta = math.radians(angulo)
            x = int(R*((1-k)*math.cos(theta)+l*k*math.cos((1-k)/k*theta)))
            y = int(R*((1-k)*math.sin(theta)-l*k*math.sin((1-k)/k*theta)))
            pygame.draw.circle(ventana, NARANJA, (x+ANCHO//2,ALTO//2-y),1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def main(): #Función principal
    r= int(input("r: "))
    R= int(input("R: "))
    l= float(input("l: "))
    dibujo= dibujarConEspirografo(r,R,l)
    print (dibujo)

main()