#Alberto Contreras Torres
#Genera figuras basadas en un espirografo


import pygame
import math


#Dibuja una figura en base a los datos, r, R, l
def dibujarEspirografo(r, R, l, r2, R2, l2, r3, R3, l3, r4, R4, l4, r5, R5, l5, r6, R6, l6):
    ANCHO = 800
    ALTO = 800
    MORADO = (200, 100, 255)
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    AZUL = (0, 0, 255)
    VERDE= (61,255,0)
    NEGRO= (0,0,0)
    CYAN= (23,84,135)
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        k= r/R
        periodo = r//math.gcd(r, R)
        for angulo in range(0, 361 * periodo, 1):
            a= math.radians(angulo)
            simplificacion= ((1-k)/k)

            x = int(R*((1-k) * math.cos(a) + l * k * (math.cos(simplificacion * a))))
            y = int(R*((1-k) * math.sin(a) - l * k * (math.sin(simplificacion * a))))
            pygame.draw.circle(ventana, ROJO, (x+ANCHO//2,ALTO//2-y), 1)


        k2= r2/R2
        periodo = r2//math.gcd(r2, R2)
        for angulo in range(0, 361 * periodo, 1):
            a2= math.radians(angulo)
            simplificacion2= ((1-k2)/k2)

            x2 = int(R2*((1-k2) * math.cos(a2) + l2 * k2 * (math.cos(simplificacion2 * a2))))
            y2 = int(R2*((1-k2) * math.sin(a2) - l2 * k2 * (math.sin(simplificacion2 * a2))))
            pygame.draw.circle(ventana, MORADO, (x2+ANCHO//2,ALTO//2-y2), 1)


        k3= r3/R3
        periodo = r3//math.gcd(r3, R3)
        for angulo in range(0, 361 * periodo, 1):
            a3= math.radians(angulo)
            simplificacion3= ((1-k2)/k2)

            x3 = int(R3*((1-k3) * math.cos(a3) + l3 * k3 * (math.cos(simplificacion3 * a3))))
            y3 = int(R3*((1-k3) * math.sin(a3) - l3 * k3 * (math.sin(simplificacion3 * a3))))
            pygame.draw.circle(ventana, AZUL, (x3+ANCHO//2,ALTO//2-y3), 1)

        k4= r4/R4
        periodo = r4//math.gcd(r4, R4)
        for angulo in range(0, 361 * periodo, 1):
            a4= math.radians(angulo)
            simplificacion4= ((1-k4)/k4)

            x4 = int(R4*((1-k4) * math.cos(a4) + l4 * k4 * (math.cos(simplificacion4 * a4))))
            y4 = int(R4*((1-k4) * math.sin(a4) - l4 * k4 * (math.sin(simplificacion4 * a4))))
            pygame.draw.circle(ventana, VERDE, (x4+ANCHO//2,ALTO//2-y4), 1)

        k5= r5/R5
        periodo = r5//math.gcd(r5, R5)
        for angulo in range(0, 361 * periodo, 1):
            a5= math.radians(angulo)
            simplificacion5= ((1-k5)/k5)

            x5 = int(R5*((1-k5) * math.cos(a5) + l5 * k5 * (math.cos(simplificacion5 * a5))))
            y5 = int(R5*((1-k5) * math.sin(a5) - l5 * k5 * (math.sin(simplificacion5 * a5))))
            pygame.draw.circle(ventana, NEGRO, (x5+ANCHO//2,ALTO//2-y5), 1)

        k6= r6/R6
        periodo = r6//math.gcd(r6, R6)
        for angulo in range(0, 361 * periodo, 1):
            a6= math.radians(angulo)
            simplificacion6= ((1-k6)/k6)

            x6 = int(R6*((1-k6) * math.cos(a6) + l6 * k6 * (math.cos(simplificacion6 * a6))))
            y6 = int(R6*((1-k6) * math.sin(a6) - l6 * k6 * (math.sin(simplificacion6 * a6))))
            pygame.draw.circle(ventana, CYAN, (x6+ANCHO//2,ALTO//2-y6), 1)


        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

# Función principal, aquí resuelves el problema
def main():
    r = int(input("Colocar valor r :"))
    R = int(input("Colocar valor R :"))
    l = float(input("Colocar valor l :"))
    r2 = int(input("Colocar valor r2 :"))
    R2 = int(input("Colocar valor R2 :"))
    l2 = float(input("Colocar valor l2 :"))
    r3 = int(input("Colocar valor r3 :"))
    R3 = int(input("Colocar valor R3 :"))
    l3 = float(input("Colocar valor l3 :"))
    r4 = int(input("Colocar valor r4 :"))
    R4 = int(input("Colocar valor R4 :"))
    l4 = float(input("Colocar valor l4 :"))
    r5 = int(input("Colocar valor r5 :"))
    R5 = int(input("Colocar valor R5 :"))
    l5 = float(input("Colocar valor l5 :"))
    r6 = int(input("Colocar valor r6 :"))
    R6 = int(input("Colocar valor R6 :"))
    l6 = float(input("Colocar valor l6 :"))
    dibujarEspirografo(r, R, l, r2, R2, l2, r3, R3, l3, r4, R4, l4, r5, R5, l5, r6, R6, l6)

# Llamas a la función principal
main()