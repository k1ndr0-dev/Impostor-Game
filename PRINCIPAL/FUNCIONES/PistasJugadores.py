#Función donde devuelve una lista con las pistas que introduce cada jugador

import os

def pistas(lista_jugadores, rondas):

    lista_pistas = []

    jugadores = len(lista_jugadores)
    x = -1
    j = 0



    lista_pistas = [[0 for _ in range (rondas)] for _ in range (jugadores)]


    for i in range (1, (jugadores * rondas) + 1):
        
        x += 1 

        print("Es el turno de: " + lista_jugadores[x])
        print("")
        dato = input("Introduce tu pista: ")
        

        #Operación matemática correcta
        if (i >= jugadores + 1):

            if (i % jugadores == 1):
                x = 0
                j += 1
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        lista_pistas[x][j] = dato

    return lista_pistas




