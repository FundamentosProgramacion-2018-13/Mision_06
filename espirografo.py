# encoding: UTF-8
# Autor: Arturo Márquez Olivar. A01376086.
# Dibuja en pygame utilizando ecuaciones paramétricas.

import math     #Librería de matemáticas.
import pygame   # Librería de pygame.


# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)
VERDE = (62, 163, 50)    # un poco de rojo, más de verde, un poco de azul
ROJO = (209, 23, 3)
CIELO = (18, 159, 243)
AZUL = (12, 12, 126)
ROSA = (255, 0, 255)


# Estructura básica de un programa que usa pygame para dibujar
#Hace el dibujo prueba de un círculo.
def dibujarCirculo(ventana):
    radio = 100
    for angulo in range(1, 361, 1):
        a = math.radians(angulo)
        x = int(radio * math.cos(a))
        y = int(radio * math.sin(a))
        pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 - y), 1)


#Dibuja usando ecuaciones paramétricas.
def dibujarEspirografo(ventana, r, R, l):
    periodo = r// math.gcd(r, R)
    k = r/R
    C = (R - r)
    P = l*r/C
    l = P*C / r

    for a in range(0, 360*periodo):
        angulo = math.radians(a)
        x = int(R * ( ((1-k)*math.cos(angulo)) + ((l*k)* math.cos(((1-k)/k) * angulo)) ))
        y = int(R * ( ((1-k)*math.sin(angulo)) - ((l*k)* math.sin(((1-k)/k) * angulo)) ))

        pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 - y), 1)


#Dibuja 3 espirógrafos con medidas ingresadas por el usuario.
def dibujarEspirografos(ventana, r, R, l, r2, R2, l2, r3, R3, l3):
    periodo = r// math.gcd(r, R)
    k = r/R
    periodo2 = r2 // math.gcd(r2, R2)
    k2 = r2/R2
    periodo3 = r3 // math.gcd(r3, R3)
    k3 = r3/R3

    for a in range(0, 360*periodo):
        angulo = math.radians(a)
        x = int(R * ( ((1-k)*math.cos(angulo)) + ((l*k)* math.cos(((1-k)/k) * angulo)) ))
        y = int(R * ( ((1-k)*math.sin(angulo)) - ((l*k)* math.sin(((1-k)/k) * angulo)) ))

        pygame.draw.circle(ventana, CIELO, (x + ANCHO//2, ALTO//2 - y), 1)

    for a in range(0, 360*periodo2):
        angulo = math.radians(a)
        x = int(R * ( ((1-k2)*math.cos(angulo)) + ((l2*k2)* math.cos(((1-k2)/k2) * angulo)) ))
        y = int(R * ( ((1-k2)*math.sin(angulo)) - ((l2*k2)* math.sin(((1-k2)/k2) * angulo)) ))

        pygame.draw.circle(ventana, AZUL, (x + ANCHO//2, ALTO//2 - y), 1)

    for a in range(0, 360*periodo3):
        angulo = math.radians(a)
        x = int(R * ( ((1-k3)*math.cos(angulo)) + ((l3*k3)* math.cos(((1-k3)/k3) * angulo)) ))
        y = int(R * ( ((1-k3)*math.sin(angulo)) - ((l3*k3)* math.sin(((1-k3)/k3) * angulo)) ))

        pygame.draw.circle(ventana, ROSA, (x + ANCHO//2, ALTO//2 - y), 1)


#Dibuja.
def dibujar(r, R, l, r2, R2, l2, r3, R3, l3):
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

        #dibujarCirculo(ventana)
        #dibujarEspirografo(ventana, r, R, l)
        dibujarEspirografos(ventana, r, R, l, r2, R2, l2, r3, R3, l3)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Teclea el radio del círculo pequeño."))
    R = int(input("Teclea el radio del círculo grande."))
    l = float(input("Teclea el valor de L."))

    r2 = int(input("Teclea el radio del segundo círculo pequeño."))
    R2 = int(input("Teclea el radio del segundo círculo grande."))
    l2 = float(input("Teclea el valor de L."))

    r3 = int(input("Teclea el radio del tercer círculo pequeño."))
    R3 = int(input("Teclea el radio del tercer círculo grande."))
    l3 = float(input("Teclea el valor de L."))


    #dibujar(r, R, l)# Por ahora, solo dibuja un espirógrafo
    dibujar(r, R, l, r2, R2, l2, r3, R3, l3) # Por ahora, solo dibuja tres estirógrafos.


# Llamas a la función principal
main()