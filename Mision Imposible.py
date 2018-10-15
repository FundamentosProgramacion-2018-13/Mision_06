#Autor: David Rodriguez
#Dibuja figuras como si fuera un espirógrafo

import pygame   # Librería de pygame
import math     #Librería de matemáticas
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
VERDE_LIMA =(0, 255, 0)
NEGRO = (0,0,0)
LILA = (199, 5, 199)
GRIS = (128, 128, 128)
# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    k = r/R
    periodo = r//math.gcd(r, R)
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
        for angulo in range(0, 360*periodo, 1):   #Convierte a radianes
            a = math.radians(angulo)
            x = int (R*((1-k) * math.cos(a) + (l*k*math.cos(((1-k)/k)*a))))
            y = int(R*((1-k) * math.sin(a) - (l*k*math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, NEGRO, (x+ANCHO//2, ALTO//2-y),1)


        r1 = r/0.420
        R1 = R*0.420
        l1 = l/0.420
        k1 = r1/R1


        for angulo in range(0, 360 * periodo, 1):  # Convierte a radianes
            a = math.radians(angulo)
            x1 = int(R1 * ((1 - k1) * math.cos(a) + (l1 * k1 * math.cos(((1 - k1) / k1) * a))))
            y1 = int(R1 * ((1 - k1) * math.sin(a) - (l1 * k1 * math.sin(((1 - k1) / k1) * a))))
            pygame.draw.circle(ventana, AZUL, (x1 + ANCHO // 2, ALTO // 2 - y1), 2)


        r3 = r*0.55
        R3 = R*0.55
        l3 = l*4
        k3 = r3 / R3


        for angulo in range(0, 360 * periodo, 1):  # Convierte a radianes
            a = math.radians(angulo)
            x3 = int(R3 * ((1 - k3) * math.cos(a) + (l3 * k3 * math.cos(((1 - k3) / k3) * a))))
            y3 = int(R3 * ((1 - k3) * math.sin(a) - (l3 * k3 * math.sin(((1 - k3) / k3) * a))))
            pygame.draw.circle(ventana, BLANCO, (x3 + ANCHO // 2, ALTO // 2 - y3), 61)


        r2 = r*0.105
        R2 = R*0.1105
        l2 = l*2.720
        k2 = r2/R2


        for angulo in range(0, 360 * periodo, 20):  # Convierte a radianes
            a = math.radians(angulo)
            x2 = int(R2 * ((1 - k2) * math.cos(a) + (l2 * k2 * math.cos(((1 - k2) / k2) * a))))
            y2 = int(R2 * ((1 - k2) * math.sin(a) - (l2 * k2 * math.sin(((1 - k2) / k2) * a))))
            pygame.draw.circle(ventana, VERDE_LIMA, (x2 + ANCHO // 2, ALTO // 2 - y2), 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Ingresa el tamaño del círculo interior: "))
    R = int(input("Ingresa el tamaño del círculo exterior:"))
    l = float(input("Ingresa el valor de l:"))
    dibujar(r, R, l)  # Por ahora, solo dibuja


# Llamas a la función principal
main()
