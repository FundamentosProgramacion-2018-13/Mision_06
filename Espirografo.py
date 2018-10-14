#Autor Claudio Mayoral Garcia
# Es un programa que dibuja como un espirografo mandando los datos de la forma en que se quiere
import pygame
import math


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO_OBSCURO = (177, 69, 99)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
GRIS = (150, 150, 150)
GRIS_OBSCURO = (100, 100, 100)


#Esta función dibuja un espirógrado al cual le tienes que asignar valores
def dibujar(r, R, l):
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
        ventana.fill(BLANCO)


        angulo = 0
        k = r/R
        for angulo in range(0, 360 * r//math.gcd(r, R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R *((((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k)/k) * a)))))
            y = int(R *((((1 - k) * math.sin(a)) - (l * k * math.sin(((1 - k)/k) * a)))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO//2, ALTO//2 + y), 1)


        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()


#Esta función dibuja un espirógrafo predeterminado
def dibujarEspirografoPre():
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
        ventana.fill(NEGRO)


        angulo = 0
        r = 65
        R = 220
        l = 0.7
        k = r/R
        for angulo in range(0, 360 * r//math.gcd(r, R)):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R *((((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k)/k) * a)))))
            y = int(R *((((1 - k) * math.sin(a)) - (l * k * math.sin(((1 - k)/k) * a)))))
            pygame.draw.circle(ventana, GRIS, (x + ANCHO//2, ALTO//2 + y), 1)


        angulo2 = 0
        r2 = 78
        R2 = 13
        l2 = 0.5
        k2 = r2 / R2
        for angulo2 in range(0, 360 * r2 // math.gcd(r2, R2)):
            b = math.radians(angulo2)
            x1 = int(R2 * ((((1 - k2) * math.cos(b)) + (l2 * k2 * math.cos(((1 - k2) / k2) * b)))))
            y1 = int(R2 * ((((1 - k2) * math.sin(b)) - (l2 * k2 * math.sin(((1 - k2) / k2) * b)))))
            pygame.draw.circle(ventana, GRIS_OBSCURO, (x1 + ANCHO // 2, ALTO // 2 + y1), 1)


        angulo3 = 0
        r3 = 50
        R3 = 280
        l3 = 0.6
        k3 = r3/R3
        for angulo3 in range(0, 360 * r3//math.gcd(r3, R3)):
            c = math.radians(angulo3)
            x2 = int(R3 *((((1 - k3) * math.cos(c)) + (l3 * k3 * math.cos(((1 - k3)/k3) * c)))))
            y2 = int(R3 *((((1 - k3) * math.sin(c)) - (l2 * k3 * math.sin(((1 - k3)/k3) * c)))))
            pygame.draw.circle(ventana, BLANCO, (x2 + ANCHO//2, ALTO//2 + y2), 1)


        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()


#Función que imprime las opciones pra elegir en el menu
def elegirOpcion():
    print("1. Dibujar espirógrafo predeterminado")
    print("2. Dibujar espirógrafo ")
    print("0. Salir ")
    opcion = int(input("¿Qué desea hacer? "))
    print("")
    return opcion


#Funcion principal
def main():
    opcion = elegirOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarEspirografoPre()
        elif opcion == 2:
            r = int(input("Escriba el valor de r"))
            R = int(input("Escriba el valor de R"))
            l = float(input("Escriba el valor de l"))
            dibujar(r, R, l)
        else:
            print("")
            print("No es una opción válida")
            print("")
        opcion = elegirOpcion()


#Llama a la función principal
main()
