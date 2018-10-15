#Autor: Jocelyn López Ortíz
#Espirógrafo

import math
import pygame

NEGRO = (0, 0, 0)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Estructura básica de un programa que usa pygame para dibujar
def calcularX(R, k, l, a):
    x = int(R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
    return x


def calcularY(R, k, l, a):
    y = int(R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
    return y


def dibujarFigura1(r, R, l, ventana):
    k = r / R
    vueltas = r // math.gcd(r, R)

    for angulo in range(0, 360 * vueltas + 1, 1):
        a = math.radians(angulo)  # Convierte a radianes
        x = calcularX(R, k, l, a)
        y = calcularY(R, k, l, a)
        pygame.draw.circle(ventana, (142, 105, 149), (x*2 + ANCHO // 2, ALTO // 2 - y*2), 1)


def dibujarFigura2(r, R, l, ventana):
    r = r*3
    l += 0.3
    k = R/ r
    vueltas = R // math.gcd(R, r)
    for angulo in range(0, 360 * vueltas + 1, 1):
        a = math.radians(angulo)  # Convierte a radianes
        x = calcularX(r, k, l, a)
        y = calcularY(r, k, l, a)
        pygame.draw.circle(ventana, (170, 140, 175), (x + ANCHO // 2, ALTO // 2 - y), 1)


def dibujarFigura3(r, R, l, ventana):
    r=r*2
    l+= 0.2
    k = R /r
    vueltas = r // math.gcd(R, r)

    for angulo in range(0, 360 * vueltas*10 , 1):
        a = math.radians(angulo)  # Convierte a radianes
        x = calcularX(r , k, l, a)
        y = calcularY(r , k, l, a)
        pygame.draw.circle(ventana, (198, 177, 201), (x * 2 // 3 + ANCHO // 2, ALTO // 2 - y * 2 // 3), 1)


def dibujar(r, R, l):
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)


        dibujarFigura1(r, R, l, ventana)
        dibujarFigura2(r, R, l, ventana)
        dibujarFigura3(r, R, l, ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()


def main():
    print("(Valores usados: 65, 220, 0.6)")
    r = int(input("Valor de r: "))
    R = int(input("Valor de R: "))
    l = float(input("Valor de l :"))
    dibujar(r, R, l)



main()