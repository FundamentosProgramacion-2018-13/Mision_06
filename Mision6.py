#Zoe Caballero Dominguez A01747247
#Espirografo que dibuja mandalas


#Librerias
import pygame
import math

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
#Colores
BLANCO = (225,225,225)
ROJO = (225,0,0)
AZUL = (36, 123, 160)
CELESTE =(112,193,179)
VERDE_CLARO = (108,201,125)
AZUL_OSCURO = (50,66,147)


#Esta es la función para dibujar la mandala que hice en la captura. Utiliza varios ciclos y varios valores.
def dibujarMandalaCaptura(ventana,r,R):
    numeroVueltas = r // math.gcd(r, R)

    #Primer círculo (contando desde el fondo).
    r = 65
    R = 220
    l = 2
    k = r / R
    for angulo in range(0, 360 * numeroVueltas, 1):
        a = math.radians(angulo)  # convierte a radianes
        x = R * (((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k) / k) * a)))
        y = R * (((1 - k) * math.sin(a)) - (l * k * math.sin(((1 - k) / k) * a)))
        pygame.draw.circle(ventana, VERDE_CLARO, (int(x) + ANCHO // 2, ALTO // 2 - int(y)), 1)

    #Segundo círculo
    l = 0.8
    R = 425
    for angulo in range(0, 360 * numeroVueltas, 1):
        a = math.radians(angulo)  # convierte a radianes
        x = R * ((k * math.cos(a)) + (l * k * math.cos(k * a)))
        y = R * ((k * math.sin(a)) - (l * k * math.sin(k * a)))
        pygame.draw.circle(ventana, CELESTE, (int(x) + ANCHO // 2, ALTO // 2 - int(y)), 1)

    #Tercer círculo
    r = 85
    R = 225
    l = .8
    k = r / R
    numeroVueltas = r // math.gcd(r, R)
    for angulo in range(0, 360 * numeroVueltas, 1):
        a = math.radians(angulo)  # convierte a radianes
        x = R * ((k * math.cos(a)) + (l * k * math.cos(k * a)))
        y = R * ((k * math.sin(a)) - (l * k * math.sin(k * a)))
        pygame.draw.circle(ventana, AZUL, (int(x) + ANCHO // 2, ALTO // 2 - int(y)), 1)

    #Cuarto círculo (el del frente)
    l = 2
    R = 85
    k = 65/220
    for angulo in range(0, 360 * numeroVueltas, 1):
        a = math.radians(angulo)  # convierte a radianes
        x = R * ((k * math.cos(a)) + (l * k * math.cos(k * a)))
        y = R * ((k * math.sin(a)) - (l * k * math.sin(k * a)))
        pygame.draw.circle(ventana, AZUL_OSCURO, (int(x) + ANCHO // 2, ALTO // 2 - int(y)), 1)


#Función dibujar: Contiene el código para pygame, dibuja la mandala con los datos dados por el usuario
# O también puede llamar a la función para dibujar la mandala de la captura.
def dibujar(r,R,l, opcion):
     pygame.init()
     ventana = pygame.display.set_mode((ANCHO, ALTO))
     reloj = pygame.time.Clock()
     termina = False

     while not termina:
         for evento in pygame.event.get():
             if evento.type == pygame.QUIT:
                 termina = True

         ventana.fill(BLANCO)

         #Aquí se dibujan las mandalas.
         if opcion == 1:
            k = r / R
            numeroVueltas = r // math.gcd(r, R)
            for angulo in range(0, 360 * numeroVueltas, 1):
                a = math.radians(angulo)  # convierte a radianes
                x = R * (((1 - k) * math.cos(a)) + (l * k * math.cos(((1 - k) / k) * a)))
                y = R * (((1 - k) * math.sin(a)) - (l * k * math.sin(((1 - k) / k) * a)))
                pygame.draw.circle(ventana, ROJO, (int(x) + ANCHO // 2, ALTO // 2 - int(y)),1)
         else:
             dibujarMandalaCaptura(ventana, r, R)

         pygame.display.flip()
         reloj.tick(40)

     pygame.quit()


#Despliega el menú y guarda la decisión del usuario, la cuál regresa a main
def leerOpcion():
    print("""¡Hola!. Bienvenido a la Misión 6.
En este programa puedes:""")
    print("1. Dibujar una figura sencilla")
    print("2. Ver la mandala de la captura.")
    print("0. Salir.")
    opcion = int(input("¿Qué te gustaría hacer? "))
    return opcion


#Funcion principal
def main():
    opcion = leerOpcion()

    while opcion != 0:
        if opcion == 1:
            r = int(input("Escribe un valor para r: "))
            R = int(input("Escribe un valor para R: "))
            l = float(input("Escribe un valor para l: "))
            dibujar(r,R,l, opcion)
        elif opcion == 2:
            r= 85
            R=225
            l=.8
            dibujar(r,R,l,opcion)
        elif opcion < 0 or opcion > 2:
            print("Por favor ingrese un número válido.")

        opcion = leerOpcion()

    print("¡Hasta pronto!")


#Llamar a la función main
main()
