# Autor: Alejandro Torices Oliva
# Es un programa que hace figuras con un espirógrafo

# import
import pygame
import math

# Dimensiones de la ventana
ALTO = 800
ANCHO = 800

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
MORADO = (255, 0, 255)
NARANJA = (255, 150, 0)


# Es la función que genera la figura
def generarEspirografo(r, R, l, COLOR):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        if COLOR != 104:
            P = r // math.gcd(r, R)
            k = r / R
            for angulo in range(360 * P + 1):
                a = math.radians(angulo)
                x = int(R * (((1 - k) * math.cos(a)) + ((l * k) * math.cos(((1 - k) / k) * a))))
                y = int(R * (((1 - k) * math.sin(a)) - ((l * k) * math.sin(((1 - k) / k) * a))))
                pygame.draw.circle(ventana, COLOR, (x + ANCHO // 2, ALTO // 2 - y), 1)
        else:
            P = r // math.gcd(r, R)
            k = r / R
            for angulo in range(360 * P + 1):
                a = math.radians(angulo)
                x = int(R * (((1 - k) * math.cos(a)) + ((l * k) * math.cos(((1 - k) / k) * a))))
                y = int(R * (((1 - k) * math.sin(a)) - ((l * k) * math.sin(((1 - k) / k) * a))))
                pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)
            k3 = .2
            for l3 in range(0, 10):
                for angulo in range(360 * 78):
                    a = math.radians(angulo)
                    x3 = int(70 * (((1 - k3) * math.cos(a)) + ((l3 * k3) * math.cos(((1 - k3) / k3) * a))))
                    y3 = int(70 * (((1 - k3) * math.sin(a)) - ((l3 * k3) * math.sin(((1 - k3) / k3) * a))))
                    pygame.draw.circle(ventana, NARANJA, (x3 + ANCHO // 2, ALTO // 2 - y3), 1)
            r1 = 99
            R1 = 50
            l1 = 3.4
            P1 = r1 // math.gcd(r1, R1)
            k1 = r1 / R1
            for angulo in range(360 * P1 + 1):
                a = math.radians(angulo)
                x1 = int(R1 * (((1 - k1) * math.cos(a)) + ((l1 * k1) * math.cos(((1 - k1) / k1) * a))))
                y1 = int(R1 * (((1 - k1) * math.sin(a)) - ((l1 * k1) * math.sin(((1 - k1) / k1) * a))))
                pygame.draw.circle(ventana, MORADO, (x1 + ANCHO // 2, ALTO // 2 - y1), 1)
            r1 = 380
            R1 = 60
            l1 = .9
            P1 = r1 // math.gcd(r1, R1)
            k1 = r1 / R1
            for angulo in range(360 * P1 + 1):
                a = math.radians(angulo)
                x1 = int(R1 * (((1 - k1) * math.cos(a)) + ((l1 * k1) * math.cos(((1 - k1) / k1) * a))))
                y1 = int(R1 * (((1 - k1) * math.sin(a)) - ((l1 * k1) * math.sin(((1 - k1) / k1) * a))))
                pygame.draw.circle(ventana, AZUL, (x1 + ANCHO // 2, ALTO // 2 - y1), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


# Es la función que genera el menú
def desplegarMenu():
    print('''
--------------------------------------------------
1. Generar figura.
2. Ver figura predeterminada.
3. Salir''')

    opcion = int(input('¿Qué desea hacer?'))
    return opcion


# Es la función que define el color de la figura
def elegirColor():
    print('')

    seleccioneColor = 'Seleccione un color'
    print(seleccioneColor.center(50, ' '))
    print('''
1. Rojo
2. Azul
3. Amarillo
4. Verde
5. Morado
6. Naranja
7. Negro
''')

    color = int(input('Color:'))
    if color == 1:
        return ROJO
    elif color == 2:
        return AZUL
    elif color == 3:
        return AMARILLO
    elif color == 4:
        return VERDE
    elif color == 5:
        return MORADO
    elif color == 6:
        return NARANJA
    elif color == 7:
        return NEGRO
    else:
        print('No es un color válido')
        return 'error'


# Es la función principal.
def main():
    titulo = ' Mision Imposible '
    titulo2 = 'Generador de mandalas'
    print(titulo.center(50, '-'))
    print(titulo2.center(50, ' '))
    print('')
    opcion = desplegarMenu()
    while opcion != 3:
        if opcion == 1:
            print('')
            r = int(input('Ingrese valor de r: '))
            R = int(input('Ingrese valor de R: '))
            l = float(input('Ingrese valor de l: '))
            COLOR = elegirColor()
            if COLOR != 'error':
                generarEspirografo(r, R, l, COLOR)
            opcion = desplegarMenu()

        elif opcion == 2:
            r = 80
            R = -150
            l = .8
            especial = 104
            generarEspirografo(r, R, l, especial)
            opcion = desplegarMenu()

        else:
            print('')
            print('error')
            opcion = desplegarMenu()

    adios = '   Termina programa   '
    print('')
    print(adios.center(50, '*'))


main()
