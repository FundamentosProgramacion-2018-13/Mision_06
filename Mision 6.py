# Francisco Ariel Arenas Enciso
# A01369122
# Desarrollo de misión 6 (dibujos con ecuaciones paramétricas mediante ciclos for, while y pygame)

'Se importan las librerías de pygame, random y math'
import pygame
import math
import random

'Se crean los parametros de la ventana'
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)


'''Esta función permite tener colores aleatorios por medio de la librería de random'''
def colores():
    colores = [random.randint(0, 255),
               random.randint(0, 255),
               random.randint(0, 255)]
    return random.choice(colores)


'''Esta función lo que permite es que se cree la figura, más no que se dibuje, asi cuando sea llamada en la función
'dibujar' ésta última no haga todo el proceso de realizar la figura.'''
def dibujarFigura(ventana,r,_R,l):
    k = (r / _R)  # Valor de k
    anguloParaEcuacion = ((1 - k) / k)  # Esta expresión representa el valor del ángulo presente en la ecuación
    periodoCirculoInterno = r // math.gcd(r, _R)  # Periodo del circulo interno. Cuántas veces hace el ciclo
    valorPeridoCompleto = periodoCirculoInterno * 360  # Para evitar tener muchas operaciones dentro del parametro de "range" se multiplca el periodo por 360
    for anguloTheta in range(0, valorPeridoCompleto + 1, 1):
        valorAnguloTheta = math.radians(anguloTheta)  # Se crea el ciclo para el ángulo
        ecuacionX = int(_R * ((1 - k) * (math.cos(valorAnguloTheta)) + l * k * (math.cos(anguloParaEcuacion * valorAnguloTheta))))  # Se transcribe la ecuación presente en el PDF
        ecuacionY = int(_R * ((1 - k) * (math.sin(valorAnguloTheta)) - l * k * (math.sin(anguloParaEcuacion * valorAnguloTheta))))  # Se transcribe la ecuación presente en el PDF
        pygame.draw.circle(ventana, colores(), ((ecuacionX + ANCHO // 2, ALTO // 2 - ecuacionY)), 1)  # No se le agrega valor de radio para que no dibuje circulos


'''Esta función es la encargada de realizar el dibujo que recibe de la función 'dibujarFigura', es decir, a través de 
las instrucciones del código de pygame, el cual se encuentra en la página del curso, realiza en una ventana de pygame el 
dibujo de la función anterior.'''
def dibujar(r, _R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:  # Ciclo principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True     # Fin de ciclo principal

        ventana.fill(BLANCO)

        dibujarFigura(ventana, r, _R, l)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

            # Después del ciclo principal
    pygame.quit()  # termina pygame


'''Función main. Ésta recibe el valor del radio del círculo interno, del círculo externo, así como el valor de 'l'
directamente del usuario'''
def main():
    r = int(input('Escribe el valor de r = '))
    _R = int(input('Escribe el valor de R = '))
    l = float(input('Escribe el valor de L = '))
    dibujar(r, _R, l)


main()