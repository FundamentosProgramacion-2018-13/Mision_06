# Rubén Villalpando Bremont
# Programa que dibuja figuras basadas en el espirógrafo.

import pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
VERDEAQUA = (14, 189, 90)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
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
        k = r/R
        periodo = r//math.gcd(r, R)
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R * ((1-k) * math.cos(a) + (l * k * math.cos(((1-k)/k)*a))))
            y = int(R * ((1-k) * math.sin(a) - (l * k * math.sin(((1-k)/k)*a))))
            pygame.draw.circle(ventana, AZUL, (x + ANCHO//2, ALTO//2 - y), 1, 1)
        r2 = r//2
        R2 = R//2
        l2 = l/2
        k2 = r2/R2
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R2 * ((1-k2) * math.cos(a) + (l2 * k2 * math.cos(((1-k2)/k2)*a))))
            y = int(R2 * ((1-k2) * math.sin(a) - (l2 * k2 * math.sin(((1-k2)/k2)*a))))
            pygame.draw.circle(ventana, VERDEAQUA, (x + ANCHO//2, ALTO//2 - y), 1, 1)
        r3 = r // 1.5
        R3 = R // 1.5
        l3 = l / 1.5
        k3 = r3 / R3
        for angulo in range(0, 360 * periodo, 1):
            a = math.radians(angulo)
            x = int(R3 * ((1 - k3) * math.cos(a) + (l3 * k3 * math.cos(((1 - k3) / k3) * a))))
            y = int(R3 * ((1 - k3) * math.sin(a) - (l3 * k3 * math.sin(((1 - k3) / k3) * a))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1, 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Valor de la r:"))
    R = int(input("Valor de la R:"))
    l = float(input("Valor de la l:"))
    dibujar(r, R, l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()