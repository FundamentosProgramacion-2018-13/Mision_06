#Luis Mario Cervantes Ortiz
#Hacer un espirógrafo con la funcion for
import pygame
import math


# Dimensiones de la pantalla
ANCHO = 1000
ALTO = 1000
# Colores
ROJO = (238, 64, 53)
NARANJA = (243, 165, 48)
VERDE= (86,185,73)
AZUL= (48,73,155)
BLANCO=(255,255,255)
def dibujar(r,R,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina= False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        circuloEspi(ventana,r,R,l)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def circuloEspi(ventana,r,R,l):
    k = r/R #el valor K
    P=r//math.gcd(r,R) #El periodo
    for angulo in range(0,360*P,1):
        a=math.radians(angulo) #El ángulo en radianes
        x = int(R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana,ROJO,(x+400,450-y),1)
        pygame.draw.circle(ventana, AZUL, (x+400, 220 - y), 1)
        pygame.draw.circle(ventana, VERDE, (x + 600, 220 + y), 1)
        pygame.draw.circle(ventana, NARANJA, (x + 600, 450 - y), 1)



def main():

    r=int(input("Valor r: "))
    R=int(input("Valor R: "))
    l=float(input("Valor L: "))

    dibujar(r,R,l)
main()