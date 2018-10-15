# encoding: UTF-8
# Autor: Oscar Alejandro Torres Maya, A01377686
# Hace un espirografo, en forma de girasol

# Librerías
import pygame   # Librería de pygame
import math     #Librería para funciones matemáticas

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
AMARILLO = (255,255,0)
NEGRO = (0,0,0)
NARANJA = (255,128,0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(R,l,r):
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
        for angulo in range(0, 361 * r//math.gcd(r, R),1):
            tetha = math.radians(angulo)
            k = r / R

            x = int(R * (1 - k) * math.cos(tetha) + ((l * k) * math.cos(((1 - k) / k) * tetha)))
            y = int(R * (1 - k) * math.sin(tetha) - ((l * k) * math.sin(((1 - k) / k) * tetha)))
            pygame.draw.circle(ventana, AMARILLO, (x + ANCHO//2 , ALTO//2 - y),5)
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2),90)
            pygame.draw.circle(ventana, NARANJA, ( x//2 + ANCHO//2, y//2 + ALTO//2), 3)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = 435
    R = 600
    l = 324

    dibujar(R,l,r)   # Por ahora, solo dibuja

# Llamas a la función principal
main()