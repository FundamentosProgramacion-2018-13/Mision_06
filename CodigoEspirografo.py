#Librerias importadas para este programa
import pygame
import math


#Dimensiones de la pantalla
ANCHO = 600
ALTO = 600


#Colores en RGB
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (59,179,34)
AZUL = (0,191,255)
ROSA = (255,20,147)
MAGENTA = (139,0,139)
LIMON = (255,250,205)
NARANJA = (255,128,0)


def dibujarFiguras():
    #Inicia motor de pygame
    pygame.init()
    #Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    reloj = pygame.time.Clock() #Usado para limitar los fps
    terminar = False #Bandera que indica si termina, inicia suponiendo que no

    while not terminar: #Ciclo principal, mientras termina sea FALSE, se repite
        #Procesa los eventos que se ponen dentro
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  #El usuario da click en cerrar
                terminar = True  #Termina el ciclo

        #Borra la pantalla con color balco cada vez que se repite el ciclo
        ventana.fill(BLANCO)

        #Figuras a trazar

        #Figura 1
        radioPequeño = 200
        radioGrande = 65
        l = 0.8
        k = radioPequeño/radioGrande
        vueltas = radioPequeño//math.gcd(radioPequeño,radioGrande)
        for angulo in range(0,360*vueltas+1):
            a = math.radians(angulo)
            x = int(radioGrande*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k)))
            y = int(radioGrande*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k)))
            pygame.draw.circle(ventana,AZUL,(x+ANCHO//2,ALTO//2-y),1)
            
        #Figura 2
        radioPequeño = 88
        radioGrande = 400
        l = 0.2
        k = radioPequeño / radioGrande
        vueltas = radioPequeño // math.gcd(radioPequeño, radioGrande)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(radioGrande * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(radioGrande * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, VERDE, (x + ANCHO // 2, ALTO // 2 - y), 2)
            
        #Figura 3
        radioPequeño = 96
        radioGrande = 147
        l = 1.8
        k = radioPequeño / radioGrande
        vueltas = radioPequeño // math.gcd(radioPequeño, radioGrande)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(radioGrande * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(radioGrande * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, NARANJA, (x + ANCHO // 2, ALTO // 2 - y), 2)
            
        #Figura 4
        radioPequeño = 19
        radioGrande = 35
        l = 14.5
        k = radioPequeño / radioGrande
        vueltas = radioPequeño // math.gcd(radioPequeño, radioGrande)
        for angulo in range(0, 360 * vueltas + 1):
            a = math.radians(angulo)
            x = int(radioGrande * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
            y = int(radioGrande * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 2)

        pygame.display.flip()   #Actualiza trazos, si está esta función no se dibuja
        reloj.tick(40) #Limita los fps a 40

    #Despues de que termina el ciclo principal
    pygame.quit()   #Termina pygame


#Corre el programa principal
dibujarFiguras()
