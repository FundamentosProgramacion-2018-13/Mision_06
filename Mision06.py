#Autor: Luis Humberto Burgueño Paz
# Realiza dibujos con espirógrafos, recibiendo los valores de r, R y l


import random   # Librería random (utilizada para generar colores)
import math     # Librería math
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujarConEspirografo(r, R, l, ventana):
    k = r / R

    for a in range(360 * r // math.gcd(r, R) + 1):
        anguloRadianes = math.radians(a)
        random1 = random.randint(1, 255)
        random2 = random.randint(1, 255)
        random3 = random.randint(1, 255)
        x = int(R * ((1 - k) * math.cos(anguloRadianes) + l * k * math.cos(((1 - k) / k) * anguloRadianes)))
        y = int(R * ((1 - k) * math.sin(anguloRadianes) - l * k * math.sin(((1 - k) / k) * anguloRadianes)))
        pygame.draw.circle(ventana, (random1, random2, random3), ((x + ALTO // 2), (ANCHO // 2 + y)), 1)


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

        dibujarConEspirografo(r, R, l, ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Teclea el valor de r: "))
    R = int(input("Teclea el valor de R:  "))
    l = float(input("Teclea el valor de l: "))
    dibujar(r, R, l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()