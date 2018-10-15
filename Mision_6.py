#Autor: Daniel Cordova Bermudez
#Grupo 02
#Descripción: Con una serie de funciones se crea figuaras geometricas.

import pygame  # Librería de pygame
import math #Librería de matematicas de python

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad


#Crea colores aleatorios.
def color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


#Dibuja la primera figura.
def figura1(ventana):


    l = 2
    radioMenor = 50
    radioMayor = 140
    k = radioMenor / radioMayor
    r = radioMenor // math.gcd(radioMenor, radioMayor)

    for angulo in range(0, 360 * r + 1):
        a = math.radians(angulo)
        x = int(radioMayor * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(radioMayor * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana, color(), (x + ANCHO // 2, ALTO // 2 - y), 1)


#Dibuja la segunda figura.
def figura2(ventana):


    l = .8
    radioMenor = 70
    radioMayor = 300
    k = radioMenor / radioMayor
    r = radioMenor // math.gcd(radioMenor, radioMayor)

    for angulo in range(0, 360 * r + 1):
        a = math.radians(angulo)
        x = int(radioMayor * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(radioMayor * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana, color(), (x + ANCHO // 2, ALTO // 2 - y), 1)


#Dibuja la tercerafigura.
def figura3(ventana):

    l = .6
    radioMenor = 5
    radioMayor = 150
    k = radioMenor / radioMayor
    r = radioMenor // math.gcd(radioMenor, radioMayor)

    for angulo in range(0, 360 * r + 1):
        a = math.radians(angulo)
        x = int(radioMayor * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(radioMayor * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana, color(), (x + ANCHO // 2, ALTO // 2 - y), 1)


#Dibuja la cuarta figura.
def figura4(ventana):

    l = .6
    radioMenor = 70
    radioMayor = 400
    k = radioMenor / radioMayor
    r = radioMenor // math.gcd(radioMenor, radioMayor)

    for angulo in range(0, 360 * r + 1):
        a = math.radians(angulo)
        x = int(radioMayor * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(radioMayor * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana,color(), (x + ANCHO // 2, ALTO // 2 - y), 1)

#Dibuja la quinta figura.
def figura5(ventana):

    l = 7
    radioMenor = 40
    radioMayor = 100
    k = radioMenor / radioMayor
    r = radioMenor // math.gcd(radioMenor, radioMayor)

    for angulo in range(0, 360 * r + 1):
        a = math.radians(angulo)
        x = int(radioMayor * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k)))
        y = int(radioMayor * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k)))
        pygame.draw.circle(ventana, color(), (x + ANCHO // 2, ALTO // 2 - y), 1)


#Inicia Pygame, llama a las funciones de para dibujar las figuras.
def dibujarEspirografo():

        # Estructura básica de un programa que usa pygame para dibujar
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
                    termina = True  # Queremos terminar el ciclo

            # Borrar pantalla
            ventana.fill(BLANCO)

            # Dibujar, aquí haces todos los trazos que requieras
            # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
            # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

            figura1(ventana)
            figura2(ventana)
            figura3(ventana)
            figura4(ventana)
            figura5(ventana)

            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
            reloj.tick(40)  # 40 fps

        # Después del ciclo principal
        pygame.quit()  # termina pygame


#Funcion main llama a la funcion que inicia pygam y dibuja las figuras.
def main():
    dibujarEspirografo()

#LLama a la funcion main.
main()