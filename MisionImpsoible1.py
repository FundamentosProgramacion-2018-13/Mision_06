#Autor: Alan Diaz Carrera
#Dibujar un espirografo con los datos otrogados por el usuario
import pygame
import math
import random



def dibujar(R,r,k,l):
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    ventana.fill(BLANCO)

    for angulo in range(0,361,10):
        R1 = R*2
        r1 = r*3
        l1 = l*1.5
        k1 = r1/R1
        a=math.radians(angulo)
        x=int(R1*(1-k1)*math.cos(a)+l1*k1*math.cos(((1-k1)/k1)*a))
        y=int(R1*(1-k1)*math.sin(a)+l1*k1*math.sin(((1-k1)/k1)*a))
        pygame.draw.circle(ventana,color2,(x+ANCHO//2,ALTO//2-y),150,1)
    for angulo in range(0,361,5):
        a=math.radians(angulo)
        x=int(R*(1-k)*math.cos(a)+l*k*math.cos(((1-k)/k)*a))
        y=int(R*(1-k)*math.sin(a)+l*k*math.sin(((1-k)/k)*a))
        pygame.draw.circle(ventana,color1,(x+ANCHO//2,ALTO//2-y),150,1)
    termina = False
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        pygame.display.flip()
    pygame.display.flip()

def main():
    R = float(input("Instroduzca el numero que desee para el radio mayor: "))
    r = float(input("Instroduzca el numero que desee para el radio menor: "))
    l = float(input("Instroduzca el numero que desee paradistancia entre puntos: "))
    k = r / R
    dibujar(R,r,k,l)
main()