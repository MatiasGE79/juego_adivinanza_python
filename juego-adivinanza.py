
import random


numero_secreto = random.randint(1,100)
adivinado = False
numero_intentos = 0
numero_maximo_intentos = 7

print("Bienvenido al juego de la adivinanza!! \nDebes lograr adivinar el numero en un maximo de: ",numero_maximo_intentos, "intentos")


while not adivinado and numero_intentos < numero_maximo_intentos :
    entrada = input("Introduce un numero del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones! has adivinado el numero secreto!")
        adivinado = True
    elif numero > numero_secreto:
        print("El numero secreto es mas bajo, vuelve a intentarlo")
    else:
        print("El numero secreto es mas alto, vuelve a intentarlo")
        

    numero_intentos +=1

if not numero_intentos < numero_maximo_intentos:
    print("No has podido adivinar el numero... GAME OVER")


