#Jesús Zabdiel Sánchez Chávez
#Dibujando con ecuaciones paramétricas. espirógrafo.

import math
import pygame
import random
def hacerEspirografo2(ventana):
    ANCHO = 800
    ALTO = 800
    NEGRO = (0, 0, 0)
    COLOR2= random.randint (0,255) , random.randint(0,255), random.randint (0,255)
    r = 65
    R = 220
    l = .8
    k = r / R
    periodo = r // math.gcd(r, R)
    disminuirOperacion = ((1 - k) / k)
    for angulo in range(0, 360 * periodo + 1, 1):
        anguloRad = math.radians(angulo)
        x = int(R * ((1 - k) * (math.cos(anguloRad)) + l * k * (math.cos(disminuirOperacion * anguloRad))))
        y = int(R * ((1 - k) * (math.sin(anguloRad)) - l * k * (math.sin(disminuirOperacion * anguloRad))))
        pygame.draw.circle(ventana, COLOR2, (x + ANCHO // 2, ALTO // 2 + y), 1)

def hacerEspirografo1(r, R, l):
    ANCHO = 800
    ALTO = 800
    NEGRO = (0, 0, 0)
    BLANCO = (250,250,250)
    COLOR1 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        k = r / R
        periodo = r //math.gcd(r, R)
        disminuirOperacion = ((1 - k) / k)
        for angulo in range(0, 360* periodo + 1,1):
            anguloRad = math.radians(angulo)
            x = int(R * ((1 - k) * (math.cos(anguloRad)) + l * k * (math.cos(disminuirOperacion* anguloRad))))
            y = int(R * ((1 - k) * (math.sin(anguloRad)) - l * k * (math.sin(disminuirOperacion * anguloRad))))
            pygame.draw.circle(ventana, COLOR1, (x + ANCHO // 2, ALTO // 2 +y), 1)

        hacerEspirografo2(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()




def main():
        r = int(input("Inserta r: "))
        R = int(input("Inserta R: "))
        l = float(input("Inserta l: "))
        hacerEspirografo1(r,R,l)

main()





