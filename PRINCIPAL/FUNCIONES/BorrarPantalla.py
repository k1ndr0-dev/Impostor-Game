import os
import time

def clean():

    os.system('cls' if os.name == 'nt' else 'clear')


def clean_espera(segundos: int):

    clean() #Limpiamos para asegurar que se quede limpia la pantalla cuando empiece la cuenta atrás

    for i in range (1, segundos+1):

        print(f"{i}...")
        time.sleep(1)
        clean()



    
        
    


