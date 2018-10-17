#Danhel Alejandro Mercado Velasco


import pygame
from math import *

VERDE_BANDERA = (27, 94, 32)
NARANJA = (239,169,119)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ANCHO = 800
ALTO = 800

def dibujar(R,r,l,cafe):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        ventana.fill(NEGRO)
        espirografo(ventana,r,R,l,VERDE_BANDERA)
        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()

def espirografo(v,r,R,l,q):
    g = r // gcd(r, R)
    for angulo in range(0,g*360+1,1):
        k = r/R
        a = radians(angulo)
        x = int(R*((1-k)* cos(a)+l*k*(cos(((1-k)/k)*a))))
        y = int(R*((1-k)* sin(a)-l*k*(sin(((1-k)/k)*a))))
        pygame.draw.circle(v, q, (x + ANCHO//2, ALTO//2-y),1)

def main():
    r = int(input("Ingresar r: "))
    R = int(input("Ingresar R: "))
    l = float(input("Ingresar l: "))
    dibujar(r,R,l, VERDE_BANDERA)
main()