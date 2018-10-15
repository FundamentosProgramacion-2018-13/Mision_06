# encoding: UTF-8
#Autor: Carlos Alberto Reyes Ortiz A0137649
#Usando de base un programa del Ing. Roberto Martínez Román en toda la parte de como dibujar en pygame

#Recrea un espirógrafo usando pygame. Se le pide al usuario tres datos para crear una figura.



from math import cos, sin, radians, gcd
import pygame # Librería de pygame
import random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO= (0,0,0)
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad



def dibujarEspirografo(r, R ,l): #Esta función en una ventana crea el dibujo que el usuario va ver.

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        colorAleatorio = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        k = r / R
        for angulo in range(361 * (r // gcd(r, R))):
            a = radians(angulo)
            x = int(R * ((1 - k) * cos(a) + l * k * cos(((1 - k) / k) * a)))
            y = int(R * ((1 - k) * sin(a) - l * k * sin(((1 - k) / k) * a)))
            pygame.draw.circle(ventana, colorAleatorio, (x + ANCHO // 2, ALTO // 2 - y), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def main(): #Función principal: Pide al usuario los datos

        r = int(input("""Dame el valor de "r": """""))
        R = int(input("""Dame el valor de "R": """""))
        l = float(input("""Dame el valor de "l": """""))

        dibujarEspirografo(r, R, l,)

main()