#Autor: Jesús Emmanuel Alcalá Nava
#Descripción: imitar un espirógrafo cuando el usuario nos da valores de r l y R

#librerías
import random
import math
import pygame

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
#Color blanco
BLANCO = (255, 255, 255)

#Formulas que usa el espirógrafo
def dibujarEspirografo(r, R, l, ventana):
    k = r / R
    for a in range(360 * r // math.gcd(r, R) + 1):
        anguloRadianes = math.radians(a)
        colorRandom1 = random.randint(1, 255)
        colorRandom2 = random.randint(1, 255)
        colorRandom3 = random.randint(1, 255)
        x = int(R * ((1 - k) * math.cos(anguloRadianes) + l * k * math.cos(((1 - k) / k) * anguloRadianes)))
        y = int(R * ((1 - k) * math.sin(anguloRadianes) - l * k * math.sin(((1 - k) / k) * anguloRadianes)))
        pygame.draw.circle(ventana, (colorRandom1, colorRandom2, colorRandom3), ((x + ALTO // 2), (ANCHO // 2 + y)), 1)


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
        dibujarEspirografo(r, R, l, ventana)
        pygame.display.flip()
        reloj.tick(10)
    pygame.quit()


def main():
    r = int(input("Teclea el valor de r: "))
    R = int(input("Teclea el valor de R:  "))
    l = float(input("Teclea el valor de l: "))
    dibujar(r, R, l)


main()