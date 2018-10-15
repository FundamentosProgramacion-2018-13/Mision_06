#Autor: Damián Iván García Ravelo
#Programa que dibuja una mandala

#Imprtar las librerias requeridas
import pygame
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#Color de la pantalla:
colorRandom = randint(0, 255), randint(0, 255), randint(0, 255)
color = (80, 90, 190)
def dibujarMandala(r,R,l):
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
        ventana.fill(color)

        colorRandom = randint(0, 100), randint(0, 100), randint(0, 100)
        for angulo in range(0,361 * (r // math.gcd(r, R))):
            a=math.radians(angulo) #Convierte a radianes
            k = r / R  # Como se obtiene k
            #Uso de formulas otorgadas por el profesor
            x= int(R * ((1 - k) * math.cos(a) + l * k * math.cos(((1 - k) / k) * a)))
            y= int(R * ((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a)))
            pygame.draw.circle(ventana, colorRandom, (x + ANCHO // 2, ALTO // 2 - y), 2)#Inicia el dibujo circular




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def main():
    #Le pregunta al usuario los valores
    r=int(input("Ingresa el valor de r: "))
    R=int(input("Ingresa el valor de R: "))
    l=float(input("Ingresa el valor de l: "))
    dibujarMandala(r,R,l)

main() #Llama a la función principal