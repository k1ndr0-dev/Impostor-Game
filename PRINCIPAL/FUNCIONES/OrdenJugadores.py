
import random
import time
from .BorrarPantalla import clean


def orden_jugadores(lista):

    lista_ordenada = lista.copy()
    random.shuffle(lista_ordenada)
    
    return lista_ordenada
        
        
def comenzar_juego():

    print("¿Cuántas rondas queréis jugar?")
    rondas = int(input("Introduce el número de rondas: "))

    for i in range(3, 0, -1):
        clean()
        print(f"El juego comienza en {i}...")
        time.sleep(1)
        

    print("¡El juego ha comenzado!")
    time.sleep(1)
    clean()
    

    return rondas




    




