#Autor: Diana Marisol Medina Bravo
import math
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Color
NEGRO=(5,5,5)
BLANCO = (255, 255, 255)
VERDE = (125, 200, 125)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Función que dibuja el epirógrafo
def hacereEpirógrafo(ventana,r,l,bigR):
    k=r/bigR
    periodo = r//math.gcd(r, bigR)

    for angulo in range(0,(360*periodo+1),1):
        a=math.radians(angulo)

        cosa = math.cos(a)
        sena = math.sin(a)
        coslk=math.cos(a*(1-k)/k)
        senlk=math.sin(a*(1-k)/k)

        x=bigR*((1-k)*cosa+(l*k)*coslk)
        y=bigR*((1-k)*sena-(l*k)*senlk)

        pygame.draw.circle(ventana, RED,(int(x)+ANCHO//2,ALTO//2-int(y)),1)


def dibujar(r, l, bigR):
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
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        hacereEpirógrafo(ventana, r, l, bigR)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Función principal
def main():
    r= int(input("Ingrese los valores de r:"))
    bigR = int(input("Ingrese los valores de R:"))
    l = float(input("Ingrese los valores de l:"))
    dibujar(r, l , bigR)

main()