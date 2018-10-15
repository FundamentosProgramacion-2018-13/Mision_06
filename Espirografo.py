# encoding: UTF-8
# Autor: Luis Armando Miranda Alcocer
# Realizar un espirógrafo

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (14, 75, 239)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)
AZUL_PANTONE = (0,24,168)
AZUL_MAYA = (115,194,251)
ORO = (250,189,0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
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


        radio = 100
        k = r / R
        for angulo in range (0, (r//math.gcd(r,R))*360+1): #Círculos Creciendo
            a= math.radians(angulo) #Pasar a radianes
            x= int(R*((1-k)*math.cos(a) +l*k*math.cos(((1-k)/k)*a)))
            y= int(R*((1-k)*math.sin(a) -l*k*math.sin(((1-k)/k)*a)))
            pygame.draw.circle(ventana, AZUL_PANTONE,(x+ANCHO // 2, ALTO//2 -y),1)
            pygame.draw.circle(ventana, AZUL, (x + ANCHO // 2, ALTO // 2 + y), 1)
            pygame.draw.circle(ventana, AZUL_MAYA, (-x + ANCHO // 2, ALTO // 2 + y), 1)

        for angulo in range (0, (r//math.gcd(r,R))*360+1): #Espiral del centro hacia afuera
            a= math.radians(angulo) #Pasar a radianes
            x= int(R*((2-k)*math.cos(a) +l*k*math.cos(((1-k)/k)*a)))
            y= int(R*((2-k)*math.sin(a) +l*k*math.sin(((1-k)/k)*a)))
            pygame.draw.circle(ventana, AZUL_PANTONE,(x+ANCHO // 2, ALTO//2 -y),1)
            pygame.draw.circle(ventana, AZUL, (-x + ANCHO // 2, ALTO // 2 + y), 1)

        reloj.tick(40)  # 40 fps
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def main():
    r= int(input("Teclea el valor de r: "))
    R= int(input("Teclea el valor de R: "))
    l= float(input("Teclea el valor de l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()