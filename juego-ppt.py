from operator import truediv
import random
from typing import List

print("Bienvenido al juego de piedra, papel o tijeras")
#----------------------------------------------------------------------------------------
seleccion_cantidad_jugadores = input("Seleccione 1 o 2 jugadores: ")
cantidad_jugadores = int(seleccion_cantidad_jugadores)
seleccion_habilitada_jugadores = [1,2]
lista = ['piedra','papel','tijeras']

while cantidad_jugadores not in seleccion_habilitada_jugadores: #BUCLE PARA EVITAR SELECCION INVALIDA DE JUGADORES
    print("Debe seleccionar 1 o 2 jugadores")
    seleccion_cantidad_jugadores = input("Seleccione 1 o 2 jugadores: ")
    cantidad_jugadores = int(seleccion_cantidad_jugadores)

#---------------------------------------------------------------------------------------
# JUEGO DE 1 JUGADOR

if cantidad_jugadores == 1:
    nombre_jugador_1 = input("Nombre jugador 1: ")
    print(nombre_jugador_1 + ", seleccione piedra, papel o tijeras:")
    seleccion_jugador1 = input()
    seleccion_jugador1_lower = seleccion_jugador1.lower()
    while seleccion_jugador1_lower not in lista:
        print(nombre_jugador_1 + ", seleccione piedra, papel o tijeras:")
        seleccion_jugador1 = input()
        seleccion_jugador1_lower = seleccion_jugador1.lower()
        
    seleccion_CPU = random.choice(lista)    
    print("Jugador CPU ha seleccionado "+ seleccion_CPU)

# condiciones que gana jugador 1
    condicion_1jugador_1 = seleccion_jugador1_lower == "tijeras" and seleccion_CPU == "papel"
    condicion_2jugador_1 = seleccion_jugador1_lower == "papel" and seleccion_CPU == "piedra"
    condicion_3jugador_1 = seleccion_jugador1_lower == "piedra" and seleccion_CPU == "tijeras"

    if seleccion_jugador1_lower == seleccion_CPU :
        print("Ha sido un empate!!!")
    elif condicion_1jugador_1 or condicion_2jugador_1 or condicion_3jugador_1:
        print("Felicitaciones!, ha ganado " + nombre_jugador_1)
    else:
        print("Perdiste! Ha ganado Jugador CPU")

#---------------------------------------------------------------------------------------
# JUEGO DE 2 JUGADORES
else:
    nombre_jugador_1 = input("Nombre jugador 1: ")
    nombre_jugador_2 = input("Nombre jugador 2: ")
    print(nombre_jugador_1 + ", seleccione piedra, papel o tijeras:")
    seleccion_jugador1 = input()
    seleccion_jugador1_lower = seleccion_jugador1.lower()
    while seleccion_jugador1_lower not in lista:
        print(nombre_jugador_1 + ", seleccione piedra, papel o tijeras:")
        seleccion_jugador1 = input()
        seleccion_jugador1_lower = seleccion_jugador1.lower()
    print(nombre_jugador_2 + ", seleccione piedra, papel o tijeras:")   
    seleccion_jugador2 = input()
    seleccion_jugador2_lower = seleccion_jugador2.lower()
    while seleccion_jugador2_lower not in lista:
        print(nombre_jugador_2 + ", seleccione piedra, papel o tijeras:")
        seleccion_jugador2 = input()
        seleccion_jugador2_lower = seleccion_jugador2.lower()
    seleccion_CPU = random.choice(lista)    
    print("Jugador CPU ha seleccionado "+ seleccion_CPU)
   
   # condiciones en los que gana jugador 1
    condicion_4jugador_1 = seleccion_jugador1_lower == "tijeras" and seleccion_CPU == "papel" and seleccion_jugador2_lower == "papel"
    condicion_5jugador_1 = seleccion_jugador1_lower == "papel" and seleccion_CPU == "piedra" and seleccion_jugador2_lower == "piedra"
    condicion_6jugador_1 = seleccion_jugador1_lower == "piedra" and seleccion_CPU == "tijeras" and seleccion_jugador2_lower == "tijeras"
    
    # condiciones en los que gana jugador 2
    condicion_1jugador_2 = seleccion_jugador2_lower == "tijeras" and seleccion_CPU == "papel" and seleccion_jugador1_lower == "papel"
    condicion_2jugador_2 = seleccion_jugador2_lower == "papel" and seleccion_CPU == "piedra" and seleccion_jugador1_lower == "piedra"
    condicion_3jugador_2 = seleccion_jugador2_lower == "piedra" and seleccion_CPU == "tijeras" and seleccion_jugador1_lower == "tijeras"
    
    # condiciones en los que empatan jugador 1 y 2
    condicion_1jugador_1_2 = seleccion_jugador2_lower == "tijeras" and seleccion_CPU == "papel" and seleccion_jugador1_lower == "tijeras"
    condicion_2jugador_1_2 = seleccion_jugador2_lower == "papel" and seleccion_CPU == "piedra" and seleccion_jugador1_lower == "papel"
    condicion_3jugador_1_2 = seleccion_jugador2_lower == "piedra" and seleccion_CPU == "tijeras" and seleccion_jugador1_lower == "piedra"
     
    # condiciones en los que empatan jugador 1 y CPU
    condicion_1jugador_1_CPU = seleccion_jugador1_lower == "tijeras" and seleccion_CPU == "tijeras" and seleccion_jugador2_lower == "papel"
    condicion_2jugador_1_CPU = seleccion_jugador1_lower == "papel" and seleccion_CPU == "papel" and seleccion_jugador2_lower == "piedra"
    condicion_3jugador_1_CPU = seleccion_jugador1_lower == "piedra" and seleccion_CPU == "piedra" and seleccion_jugador2_lower == "tijeras"
    
    # condiciones en los que empatan jugador 2 y CPU
    condicion_1jugador_2_CPU = seleccion_jugador2_lower == "tijeras" and seleccion_CPU == "tijeras" and seleccion_jugador1_lower == "papel"
    condicion_2jugador_2_CPU = seleccion_jugador2_lower == "papel" and seleccion_CPU == "papel" and seleccion_jugador1_lower == "piedra"
    condicion_3jugador_2_CPU = seleccion_jugador2_lower == "piedra" and seleccion_CPU == "piedra" and seleccion_jugador1_lower == "tijeras"

    if seleccion_jugador1_lower == seleccion_CPU == seleccion_jugador2_lower:
        print("Ha sido un empate!!!")
    elif condicion_4jugador_1 or condicion_5jugador_1 or condicion_6jugador_1:
        print("Felicitaciones!, ha ganado " + nombre_jugador_1)
    elif condicion_1jugador_2 or condicion_2jugador_2 or condicion_3jugador_2:
        print("Felicitaciones!, ha ganado " + nombre_jugador_2)
    elif condicion_1jugador_1_CPU or condicion_2jugador_1_CPU or condicion_3jugador_1_CPU:
        print("Felicitaciones!, han ganado jugador CPU y " + nombre_jugador_1)
    elif condicion_1jugador_2_CPU or condicion_2jugador_2_CPU or condicion_3jugador_2_CPU:
        print("Felicitaciones!, han ganado jugador CPU y " + nombre_jugador_2)
    else:
        print("Han empatado todos los jugadores!!")
