# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que dibuja círculos para crear figuras basadas en espirógrafos usando ecuaciones paramétricas.

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)

# La siguiente función genera colores aleatorios.
def color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def obtenerX(variableR, variabler, variablel)

def dibujarCirculos(variableR, variabler, variablel, color, angulo):
    periodo = variabler // math.gcd(variabler, variableR)
    o = math.radians(angulo)
    k = variabler / variableR
    x = variableR((variablel - k)*math.cos(o)+variablel*k*math.cos((variablel-k/k)*o))
    y = variableR((variablel - k)*math.sin(o)-variablel*k*math.sin((variablel-k/k)*o))


    for h in range(0, 360 * periodo):



# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
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

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        radio = 100
        for angulo in range(0, 360 + 1, 1):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja
    variableR = float(input("Teclea el valor de R: "))
    variabler = float(input("Teclea el valor de r: "))
    variablel = float(input("Teclea el valor de l: "))





# Llamas a la función principal
main()
