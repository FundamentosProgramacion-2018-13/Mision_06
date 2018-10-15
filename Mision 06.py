# Autor: Oscar Macias Rodríguez - A01376398
# Descripción: Dibuja la curva generada por un espirógrafo.


# Importa librerías.
import pygame
import math


# Tamaño de la pantalla.
ANCHO = 800
ALTO = 800


# Colores.
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (200, 200, 0)
AZUL = (0, 140, 140)
VERDE = (0, 200, 0)


# Dibuja la figura central.
def dibujarFigura1(ventana):
    r = 78
    R = 30
    l = 0.4

    for angulo in range(0, 7*360+1, 1):
        k = r / R
        a = math.radians(angulo)
        z = r // math.gcd(r, R)
        a = 2*a + z
        x = int(R*((1 - k) * math.cos(a) + (l * k) * (math.cos((1 - k) / k * a))))
        y = int(R*((1 - k) * math.sin(a) + (l * k) * (math.sin((1 - k) / k * a))))

        pygame.draw.circle(ventana, VERDE, (x + ANCHO//2, ALTO//2 - y), 1)


# Dibuja la figura de átomo.
def dibujarFigura2(ventana):
    r = 150
    R = 30
    l = 0.6

    for angulo in range(0, 7*360+1, 1):
        k = r / R
        a = math.radians(angulo)
        z = r // math.gcd(r, R)
        a = a + z
        x = int(R*((1 - k) * math.cos(a) + (l * k) * (math.cos((1 - k) / k * a))))
        y = int(R*((1 - k) * math.sin(a) + (l * k) * (math.sin((1 - k) / k * a))))

        pygame.draw.circle(ventana, AMARILLO, (x + ANCHO//2, ALTO//2 - y), 1)


# Dibuja el círculo blanco.
def dibujarFigura3(ventana):
    r = 65
    R = 200
    l = 0.8

    for angulo in range(0, 70*360+1, 1):
        k = r / R
        a = math.radians(angulo)
        z = r // math.gcd(r, R)
        a = 3*a**2 + z
        x = int(R*((1 - k) * math.cos(a) + (l * k) * (math.cos((1 - k) / k * a))))
        y = int(R*((1 - k) * math.sin(a) + (l * k) * (math.sin((1 - k) / k * a))))

        pygame.draw.circle(ventana, BLANCO, (x + ANCHO//2, ALTO//2 - y), 1)


# Dibuja la figura que parece flor.
def dibujarFigura4(ventana):
    r = 25
    R = 300
    l = 2

    for angulo in range(0, 70*360+1, 1):
        k = r / R
        a = math.radians(angulo)
        z = r // math.gcd(r, R)
        a = a**2 + z
        x = int(R*((1 - k) * math.cos(a) + (l * k) * (math.cos((1 - k) / k * a))))
        y = int(R*((1 - k) * math.sin(a) + (l * k) * (math.sin((1 - k) / k * a))))

        pygame.draw.circle(ventana, AZUL, (x + ANCHO//2, ALTO//2 - y), 1)


# Dibuja todas las funciones previas.
def dibujarEspirógrafo():
    # Inicializa el motor de pygame
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.display.set_caption("Mision 6. Espirógrafo")  # Nombra la ventana

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(NEGRO)  # Colorea la ventana

        dibujarFigura1(ventana)  # Llama a la función
        dibujarFigura2(ventana)  # Llama a la función
        dibujarFigura3(ventana)  # Llama a la función
        dibujarFigura4(ventana)  # Llama a la función

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Llama a la función main.
def main():
    dibujarEspirógrafo()


main()