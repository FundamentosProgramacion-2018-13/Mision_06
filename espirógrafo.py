#Autor:Samantha Martínez Franco     A01747686
#Descripción: Utilizar ciclos for para crear un espirografo


import pygame   # Librería de pygame
import math


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800


# Colores
BLANCO=(255,255,255)
AZUL = (102,0, 51)      # nada de rojo, ni verde, solo azul
ROSA= (102,0,102)
MORADO=(51,0,102)

#función que dibuja utilizando las ecuaciones de un espirografo
def dibujarEspirografo(ventana, r, R, l,r2,R2,l2,r3,R3,l3):
    k=r/R

    #circulo 1
    for angulo in range(0, 360*r//math.gcd(r, R)):
        a=math.radians(angulo)
        x=int(R*((1-k)*math.cos(a)+l*k*math.cos(((1-k)/k)*a)))
        y = int(R * ((1 - k) * math.sin(a) - l * k * math.sin(((1 - k) / k) * a)))
        pygame.draw.circle(ventana,AZUL,(x+ANCHO//2, ALTO//2-y),1)

    #circulo 2
    k2=r2/R2
    for angulo2 in range(0, 360*r2//math.gcd(r2, R2)):
        a2=math.radians(angulo2)
        x=int(R2*((1-k2)*math.cos(a2)+l2*k2*math.cos(((1-k2)/k2)*a2)))
        y = int(R2 * ((1 - k2) * math.sin(a2) - l2 * k2 * math.sin(((1 - k2) / k2) * a2)))
        pygame.draw.circle(ventana,ROSA,(x+ANCHO//2, ALTO//2-y),1)

    #circulo 3
    k3 = r3 / R3
    for angulo3 in range(0, 360 * r3 // math.gcd(r3, R3)):
        a3 = math.radians(angulo3)
        x = int(R3 * ((1 - k3) * math.cos(a3) + l3 * k3 * math.cos(((1 - k3) / k3) * a3)))
        y = int(R3 * ((1 - k3) * math.sin(a3) - l3 * k3 * math.sin(((1 - k3) / k3) * a3)))
        pygame.draw.circle(ventana, MORADO,(x + ANCHO // 2, ALTO // 2 - y), 1)



# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l,r2,R2,l2,r3,R3,l3):
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
        dibujarEspirografo(ventana,r,R,l,r2,R2,l2,r3,R3,l3)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    print("Primero")    #azul
    r = int(input("r= "))   #230
    R = int(input("R= "))   #160
    l = float(input("l= "))   #0.3

    print("Segundo:")     #rosa
    r2 = int(input("r= "))  # 145
    R2 = int(input("R= "))  # 20
    l2 = float(input("l= ")) #0.5

    print("Tercero")           #Morado
    r3 = int(input("r= "))     # 145
    R3 = int(input("R= "))     # 350
    l3 = float(input("l= "))   #0.5
    dibujar(r, R, l, r2, R2, l2, r3, R3, l3)





# Llamas a la función principal
main()