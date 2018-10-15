# Alex Fernando Leyva Martínez, A01747078, 04
# Esta función realiza una figura

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)# R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
ROJO_OBSCURO = (177, 69, 99)
VERDE_BANDERA = (27, 94, 32)
VERDE_CLARO = (173, 255, 47)
AZUL_CLARO = (0,191,255)
AMARILLO_ORO = (255,215,0)
CAFE = (160,82,45)
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
GRIS = (150, 150, 150)
GRIS_OBSCURO = (100, 100, 100)

# Estructura básica de un programa que usa pygame para dibujar
def dibujarEspirografoEstandar(r,R,l):
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
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras

        k = r / R
        for angulo in range(0, 360*r//math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R* ((((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k)/k) * a)))))
            y = int(R* ((((1 - k) * math.sin(a)) - (l * k * math.sin(((1-k)/k) * a )))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 + y), 1)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(30)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspirografo():
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
        ventana.fill(BLANCO)
        # Dibujar, aquí haces todos los trazos que requieras

        r = 35
        R = 335
        l = 1
        k = r / R
        for angulo in range(0, 360*r//math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R* ((((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k)/k) * a)))))
            y = int(R* ((((1 - k) * math.sin(a)) - (l * k * math.sin(((1-k)/k) * a )))))
            pygame.draw.circle(ventana, AMARILLO_ORO, (x + ANCHO // 2, ALTO // 2 + y), 1)

        r2 = 35
        R2 = 275
        l2 = 0.5
        k2 = r2 / R2
        for angulo in range(0, 360 * r2 // math.gcd(r2, R2)):
            a = math.radians(angulo)
            x = int(R2 * ((((1 - k2) * math.cos(a)) + (l2 * k2* math.cos(((1 - k2) / k2) * a)))))
            y = int(R2* ((((1 - k2) * math.sin(a)) - (l2 * k2 * math.sin(((1 - k2) / k2) * a)))))
            pygame.draw.circle(ventana, AZUL_CLARO, (x + ANCHO // 2, ALTO // 2 + y), 1)

        r3 = 34
        R3 = 214
        l3 = 1.5
        k3 = r3 / R3
        for angulo in range(0, 360 * r3 // math.gcd(r3, R3)):
            a = math.radians(angulo)
            x = int(R3 * ((((1 - k3) * math.cos(a)) + (l3 * k3 * math.cos(((1 - k3) / k3) * a)))))
            y = int(R3 * ((((1 - k3) * math.sin(a)) - (l3 * k3 * math.sin(((1 - k3) / k3) * a)))))
            pygame.draw.circle(ventana, VERDE_CLARO, (x + ANCHO // 2, ALTO // 2 + y), 1)

        r4 = 70
        R4 = 7
        l4 = 0.8
        k4 = r4 / R4
        for angulo in range(0, 360 * r4 // math.gcd(r4, R4)):
            a = math.radians(angulo)
            x = int(R4 * ((((1 - k4) * math.cos(a)) + (l4 * k4 * math.cos(((1 - k4) / k4) * a)))))
            y = int(R4 * ((((1 - k4) * math.sin(a)) - (l4 * k4 * math.sin(((1 - k4) / k4) * a)))))
            pygame.draw.circle(ventana, CAFE, (x + ANCHO // 2, ALTO // 2 + y), 1)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(30)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame




def mostrarMenu():
    print("Selecciona alguna de las siguientes opciones:")
    print("1.Espirógrafo Estándar")
    print("2.Espirógrafo Personalizado")
    print("0. Salir")
    opcion = int(input("Qué desea hacer?"))
    return opcion

# Función principal, aquí resuelves el problema
def main():
    opcion = mostrarMenu()
    while opcion != 0:
        if opcion == 1:
            r = int(float(input("Teclea el valor de r: ")))
            R = int(float(input("Teclea el valor de R: ")))
            l = float(input("Teclea el valor de l: "))
            dibujarEspirografoEstandar(r, R, l)
        elif opcion == 2:
            dibujarEspirografo()
        else:
            print("Error, selecciona de nuevo")
            print("--------")
        main()
    print("Termina Programa. Gracias")


# Llamas a la función principal
main()

