# Autor: Michelle Sánchez Guerrero
# Descripción: Dibuja figuras como espirógrafo.


import pygame  # Librería de pygame
import math

ANCHO = 600
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
PURPURA = (197, 17, 98)
VERDE_LIMON = (118, 255, 3)
NARANJA = (255, 143, 0)
AQUA = (0, 230, 118)
AZUL_CLARO = (0, 191, 165)
MORADO = (86, 104, 200)
AMARILLO = (255, 234, 0)
ROSA = (255, 64, 129)


# Función que dibuja. Estructura básica de un programa que usa pygame para dibujar
def dibujar(r1, R1, l1, r2, R2, l2, r3, R3, l3, r4, R4, l4, r5, R5, l5):
    pygame.init()

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

                # Borrar pantalla
        ventana.fill(BLANCO)

        radio = 100
        k1 = r1 / R1
        k2 = r2 / R2
        k3 = r3 / R3
        k4 = r4 / R4
        k5 = r5 / R5
        vueltas1 = r1 // math.gcd(r1, R1)
        vueltas2 = r2 // math.gcd(r2, R2)
        vueltas3 = r3 // math.gcd(r3, R3)
        vueltas4 = r4 // math.gcd(r4, R4)
        vueltas5 = r5 // math.gcd(r5, R5)

        for angulo1 in range(0, vueltas1 * 360, 1):
            a1 = math.radians(angulo1)
            x1 = int(R1 * ((1 - k1) * math.cos(a1) + l1 * k1 * math.cos(((1 - k1) / k1) * a1)))
            y1 = int(R1 * ((1 - k1) * math.sin(a1) - l1 * k1 * math.sin(((1 - k1) / k1) * a1)))
            pygame.draw.circle(ventana, ROSA, (x1 + ANCHO // 2, ALTO // 2 - y1), 1)

        for angulo2 in range(0, vueltas2 * 360, 1):
            a2 = math.radians(angulo2)
            x2 = int(R2 * ((1 - k2) * math.cos(a2) + l2 * k2 * math.cos(((1 - k2) / k2) * a2)))
            y2 = int(R2 * ((1 - k2) * math.sin(a2) - l2 * k2 * math.sin(((1 - k2) / k2) * a2)))
            pygame.draw.circle(ventana, NARANJA, (x2 + ANCHO // 2, ALTO // 2 - y2), 1)

        for angulo3 in range(0, vueltas3 * 360, 1):
            a3 = math.radians(angulo3)
            x3 = int(R3 * ((1 - k3) * math.cos(a3) + l3 * k3 * math.cos(((1 - k3) / k3) * a3)))
            y3 = int(R3 * ((1 - k3) * math.sin(a3) - l3 * k3 * math.sin(((1 - k3) / k3) * a3)))
            pygame.draw.circle(ventana, VERDE_LIMON, (x3 + ANCHO // 2, ALTO // 2 - y3), 1)

        for angulo4 in range(0, vueltas4 * 360, 1):
            a4 = math.radians(angulo4)
            x4 = int(R4 * ((1 - k4) * math.cos(a4) + l4 * k4 * math.cos(((1 - k4) / k4) * a4)))
            y4 = int(R4 * ((1 - k4) * math.sin(a4) - l4 * k4 * math.sin(((1 - k4) / k4) * a4)))
            pygame.draw.circle(ventana, AZUL_CLARO, (x4 + ANCHO // 2, ALTO // 2 - y4), 1)

        for angulo5 in range(0, vueltas5 * 360, 1):
            a5 = math.radians(angulo5)
            x5 = int(R5 * ((1 - k5) * math.cos(a5) + l5 * k5 * math.cos(((1 - k5) / k5) * a5)))
            y5 = int(R5 * ((1 - k5) * math.sin(a5) - l5 * k5 * math.sin(((1 - k5) / k5) * a5)))
            pygame.draw.circle(ventana, AZUL_CLARO, (x5 + ANCHO // 2, ALTO // 2 - y5), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# Función principal. Lee e imprime datos
def main():
    print("Para dibujar, ingresa los valores de r, R y l")
    print("Figura 1")
    r1 = int(input("r: "))  # 20
    R1 = int(input("R: "))  # 150
    l1 = float(input("l: "))  # 2

    print("Figura 2")
    r2 = int(input("r: "))  # 20
    R2 = int(input("R: "))  # 150
    l2 = float(input("l: "))  # 5

    print("Figura 3")
    r3 = int(input("r: "))  # 5
    R3 = int(input("R: "))  # 14
    l3 = float(input("l: "))  # 1

    print("Figura 4")
    r4 = int(input("r: "))  # 58
    R4 = int(input("R: "))  # 62
    l4 = float(input("l: "))  # 1

    print("Figura 5")
    r5 = int(input("r: "))  # 95
    R5 = int(input("R: "))  # 97
    l5 = float(input("l: "))  # 2

    dibujar(r1, R1, l1, r2, R2, l2, r3, R3, l3, r4, R4, l4, r5, R5, l5)


# Llamar a la función principal
main()