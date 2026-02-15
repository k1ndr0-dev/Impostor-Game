from .JugadoresPistas import imprimir
from FUNCIONES.BorrarPantalla import clean


def votacion(diccionario: dict) -> list:

    copia_diccionario = diccionario.copy() #Se guardan los jugadores a los que se pueden votar

    lista_jugadores = list(diccionario.copy().keys())  #Guarda los jugadores que pueden votar (no nominados)

    diccionario_votos = dict.fromkeys(diccionario.keys(), 0) #Diccionario que cuenta los votos

    jugadores_eliminados = [] #Guarda los jugadores eliminados 


    #Bucle hasta conseguir un jugador eliminado
    while True:
        
        #Imprimimos a los jugadores que se pueden nominar
        imprimir(copia_diccionario)


        #Recorremos la lista donde se guardan los jugadores que pueden votar
        for jugador in lista_jugadores:
            
            print(f"{jugador}, vota")
            
            #Comprobar si el jugador introduce un número correcto
            while True:

                voto = input(f"Introduce el número del jugador que quieres votar: ")

                try:

                    voto = int(voto)

                    if 1 <= voto <= len(copia_diccionario):
                        break
                    else:
                        print(f"Número fuera de rango, introduzca un número entre 1 y {len(copia_diccionario)}")

                except ValueError:
                    print(f"Carácter inválido")



            diccionario_votos[list(copia_diccionario.keys())[voto - 1]] += 1 #Aumentamos un voto al jugador elegido

        clean()
        
        maximo_votos = max(diccionario_votos.values()) #Sacamos el máximo de votos

        #Guarda dentro de una lista los jugadores que tengan el número máximo de votos
        jugadores_eliminados = [

            jugador
            for jugador, votos in diccionario_votos.items()
            if votos == maximo_votos
        ]
        


        
        if len(jugadores_eliminados) == 1: #Si solo hay un eliminado

            break #Salimos del bucle al tener ya un eliminado

        else:
           
           #Guardamos a los jugadores nominados
           copia_diccionario = {
               
            jugador: diccionario[jugador]
            for jugador in diccionario
            if jugador in jugadores_eliminados

            }
           
           #Guardamos a los jugadores no nominados
           lista_jugadores = [
               
            jugador
            for jugador in diccionario.keys()
            if jugador not in jugadores_eliminados

           ]

    
    return jugadores_eliminados #Sale un solo jugador
           

