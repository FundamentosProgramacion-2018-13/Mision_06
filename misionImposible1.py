# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 1920
ALTO = 1080
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0,0,255) # nada de rojo, ni verde, solo azul
VERDE = (0,255,0)
NARANJA = (255,128,0)
COLORS = [AZUL, NARANJA, VERDE, ROJO]


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(data, rep):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    time = 1
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        for x in range(rep):
            mandala(data[x][0], data[x][1], data[x][2], x, ventana)
        
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        
    # Después    del ciclo principal
    pygame.quit()  # termina pygame

def mandala(r, R, l, rep, ventana):
    k=r/R
    for angr in range(360*(r//math.gcd(r,R))+1):
        ang = math.radians(angr)
        x = int(R*((1-k)*math.cos(ang)+l*k*math.cos(((1-k)/k)*ang)))
        y = int(R*((1-k)*math.sin(ang)-l*k*math.sin(((1-k)/k)*ang)))
        pygame.draw.circle(ventana, COLORS[rep], (x+ANCHO//2,ALTO//2-y), 1)

# Función principal, aquí resuelves el problema
def main():    
    data = []
    rep = 1
    while(rep!=0):
        rep = int(input("Ingrese numero de mandalas: "))
        for i in range(rep):
            r = int(input("Ingrese r: "))
            R = int(input("Ingrese R: "))
            l = float(input("Ingrese l: "))
            data.append([r, R, l])
        dibujar(data, rep)   # Por ahora, solo dibuja


# Llamas a la función principal
main()
