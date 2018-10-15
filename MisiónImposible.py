# Autor: Luisa Fernanda Arellano Alvarado A01377974
# Dibujar diseño Espirografo, creativo con ayuda de while y for

import pygame # llama a pygame
import math   # llama a math, librería que ayuda a realizar operaciones matemáticas

# medidas
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (59, 179, 34)
AZUL = (32,178,170)
ROSA = (255,20,147)
VIOLETA = (148,0,211)
NARANJA = (124,252,0)
CAFE = (138,54,15)
SALMON = (255,64,64)
AMARILLO = (255,128,0) # naranja

def dibujarEspirografo():
    # Inicia motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()  # Usado para limitar los fps
    terminar = False  # Bandera que indica si termina, inicia suponiendo que no
    while not terminar:  # Ciclo principal, mientras termina sea FALSE, se repite
        # Procesa los eventos que se ponen dentro
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario da click en cerrar
                terminar = True  # Termina el ciclo
        # Borra la pantalla con color balco cada vez que se repite el ciclo
        ventana.fill(BLANCO)

         # Flor azul
        valorR1 = 120 # valor del primer radio
        valorR2 = 70   # valor del segundo radio
        l = 0.8 # valor de l para usar en la formula dada por el profesor
        k = valorR1 / valorR2# valor de K para usar en la formula dada por el profesor
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, AZUL, (x + ANCHO // 2, ALTO // 2 - y), 1)

         # Estrella gigante deforme

        valorR1 = 100
        valorR2 = 450
        l = 0.6
        k = valorR1 / valorR2
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 2)

            # circulo verde

            valorR1 = 150
            valorR2 = 230
            l = 1.5
            k = valorR1 / valorR2
            vueltas = valorR1 // math.gcd(valorR1, valorR2)
            for angulo in range(0, 360 * vueltas + 1):
                a = math.radians(angulo)
                x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
                y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
                pygame.draw.circle(ventana, SALMON, (x + ANCHO // 2, ALTO // 2 - y), 2)


       # Flor rosa alrededor de flor azul
        valorR1 = 155
        valorR2 = 80
        l = 1.10
        k = valorR1 / valorR2
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, ROSA, (x + ANCHO // 2, ALTO // 2 - y), 2)





       # flor punteada larga
        valorR1 = 96
        valorR2 = 147
        l = 2
        k = valorR1 / valorR2
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, NARANJA, (x + ANCHO // 2, ALTO // 2 - y), 2)


        # Circulo Uno café
        valorR1 = 19
        valorR2 = 35
        l = 13
        k = valorR1 / valorR2
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana,CAFE, (x + ANCHO // 2, ALTO // 2 - y), 2)

        # Circulo dos color  naranja
        valorR1 = 19
        valorR2 = 35
        l = 15
        k = valorR1 / valorR2
        vueltas = valorR1 // math.gcd(valorR1, valorR2)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(valorR2 * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(valorR2 * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, AMARILLO, (x + ANCHO // 2, ALTO // 2 - y), 2)

        pygame.display.flip()  # Actualiza trazos, si está esta función no se dibuja
        reloj.tick(40)  # Limita los fps a 40



pygame.quit()  # Termina pygame

dibujarEspirografo() # llamar a la función