#Jose Luis Mata Lomelí
#Crear dibujos tipo espirografo

import pygame
import math
import random

#Dimensiones
Ancho = 800
Alto = 800

#Colores
BLANCO = (255, 255, 255)

def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de Ancho * Alto
    ventana = pygame.display.set_mode((Ancho, Alto))  # Crea la ventana donde dibujara
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecucion, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automÃ¡ticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botÃ³n de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)


        k = r/R
        periodo = r//math.gcd(r, R)

        #color
        colorrandom1 = (random.randrange(255), random.randrange(255), random.randrange(255))
        colorrandom2 = (random.randrange(255), random.randrange(255), random.randrange(255))
        colorrandom3 = (random.randrange(255), random.randrange(255), random.randrange(255))
        colorrandom4 = (random.randrange(255), random.randrange(255), random.randrange(255))

        #circulo 1
        u = r * 2
        U = R * 2
        o = l * 2
        p = u / U

        #circulo 2
        f = r * 3
        F = R * 3
        h = l * 3
        j = f / F

        #circulo 3
        z = r * 4
        Z = R * 4
        v = l * 4
        b = z / Z


#Primer Circulo

        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-k) * math.cos(a) + (l * k * math.cos(((1-k)/k)*a))))
            y = int(R * ((1-k) * math.sin(a) - (l * k * math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, colorrandom1, (x + Ancho//2, Alto//2 - y), 1, 1)

#Segundo Circulo

        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-p) * math.cos(a) + (o * p * math.cos(((1-p)/p)*a))))
            y = int(R * ((1-p) * math.sin(a) - (o * p * math.sin(((1-p)/p)*a))))
            pygame.draw.circle(ventana, colorrandom2, (x + Ancho//2, Alto//2 - y), 1, 1)

#Tercer Circulo

        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-j) * math.cos(a) + (h * j * math.cos(((1-j)/j)*a))))
            y = int(R * ((1-j) * math.sin(a) - (h * j * math.sin(((1-j)/j)*a))))
            pygame.draw.circle(ventana, colorrandom3, (x + Ancho//2, Alto//2 - y), 1, 1)

#Cuarto Circulo

        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-b) * math.cos(a) + (v * b * math.cos(((1-b)/b)*a))))
            y = int(R * ((1-b) * math.sin(a) - (v * b * math.sin(((1-b)/b)*a))))
            pygame.draw.circle(ventana, colorrandom4, (x + Ancho//2, Alto//2 - y), 1, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta funcion, entonces no se dibuja)
        reloj.tick(1)

    pygame.quit()  # termina pygame


# Funcion principal
def main():

    r = int(input("Valor de r: "))
    R = int(input("Valor de R: "))
    l = float(input("Valor de l: "))
    dibujar(r, R, l)   # Aplicar la funcion y dibujar

main()
