#Autor: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Grupo 02.
#Descripción: Este programa recibe los valores necesarios, dados por el usuario, para dibujar una curva generada por
#un espirógrafo. Estas figuras se dibujan utilizando ecuaciones paramétricas que representan valores en el plano.
#----------------------------------------------------------------------------------------------------------------------

#Se importa la libreía pygame, así como los módulos math y random.
import pygame
import math
import random

#Se declara el color blanco con sus valores RGB correspondientes. También se dan los valores del ancho y alto de la
#ventana donde se dibujarán las figuras.
BLANCO = (255, 255, 255)
ANCHO = 800
ALTO = 800


#Se declara la función dibujar que recibe como parámetros el valor de r, R y l dados por el usuario. Esta función
#contiene el código general para empezar a correr pygame. Se declara el valor de la variable k con base en los valores
#de r y R dados por el usuario. La función calcula los valores de 'x' y 'y' con base en una fórmula dada. Esto se hace
#por medio de un ciclo for. Por último, esta función dibuja los círculos necesarios para trazar la figura, pero lo hace
#alternando aleatoriamente entre 4 colores que son declarados y agregados a una lista (para hacer referencia a esta)
#dentro de la misma función.
def dibujar(r, R, l):

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        k = r/R

        for angulo in range(0, 360 * r//math.gcd(r, R)):

            COLORA = (136, 78, 160)
            COLORB = (93, 173, 226)
            COLORC = (46, 134, 193)
            COLORD = (91, 44, 111)

            colorList = []
            colorList.append(COLORA)
            colorList.append(COLORB)
            colorList.append(COLORC)
            colorList.append(COLORD)

            θ = math.radians(angulo) # Se convierten los grados a radianes.

            x = int(R*(((1-k)*math.cos(θ))+((l*k)*math.cos((((1 - k)/(k)) * θ))))) #Fórmula correspondiente al valor x.

            y = int(R*(((1-k)*math.sin(θ))-((l*k)*math.sin((((1 - k)/(k)) * θ))))) #Fórmula correspondiente al valor y.

            pygame.draw.circle(ventana, random.choice(colorList), ((x + ALTO // 2) , (ANCHO // 2 + y)), 1)

        pygame.display.flip() #Actualiza los trazos.
        reloj.tick(60) #60 fps.

    pygame.quit()  # terminar pygame


#Se declara la función main. Se le pide al usuario que teclee los valores de r, R y l para que se dibuje la figura.
#Se escribe un mensaje de error si el usuario teclea u 0 en los valores de r y R ya que en las fórmulas para calcular
#los valores de 'x' y 'y' no se puede dividir entre 0. Los valores de r, R y l se envían a la función dibujar para que
#esta otra haga los cálculos necesarios. Al final, se imprime un mensaje agradeciendo al usuario el haber usado el
#programa antes de que este se cierre.
def main():

    r = int(float(input("Escriba el valor de r: ")))
    R = int(float(input("Escriba el valor de R: ")))
    l = float(input("Escriba el valor de L: "))

    if r == 0 or R == 0:
        print("Ha escrito algún valor no válido, inténtelo de nuevo...")
        main()

    dibujar(r, R, l)

    salir = input("Gracias por haber usado el programa. Presione la tecla enter para salir...")


#Se llama a la función main para que se ejecute el programa.
main()