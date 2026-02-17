
#FUNCIONES DEL PROGRAMA PRINCIPAL

#Lista de palabras
from FUNCIONES.lista_palabras import palabras_funcion, palabras
from FUNCIONES.CamiarNombre import renombrar_repetidos

#Jugadores
from FUNCIONES.nombres import instrucciones, funcion_lista_jugadores

#Orden de los jugadores
from FUNCIONES.OrdenJugadores import orden_jugadores, comenzar_juego

#Civiles e impostor
from FUNCIONES.CivilesImpostor import impostor

#Decir palabras a cada jugador
from FUNCIONES.PalabrasJugadores_2 import PalabrasJugadores

#Meter pistas
from FUNCIONES.MeterPistas import MeterPistas  

#Votar
from FUNCIONES.FUNCIONESVOTAR import EliminarJugador,votacion_ext

#Continuar o finalizar
from FUNCIONES.Continuar import continuar


#EXTRA
from FUNCIONES.BorrarPantalla import clean, clean_espera
import time


#PROGRAMA PRINCIPAL

while True:

    #1. Instrucciones
    #2. Meter jugadores

    instrucciones()
    lista_de_jugadores = renombrar_repetidos(funcion_lista_jugadores()) 


    #Borrar pantalla
    clean_espera(3)





    #3. Jugadores civiles e impostor 
    # COMENTAR

    impostor_jugador = impostor(lista_de_jugadores)



    #4. Palabras civiles e impostor
    #COMENTAR

    palabra_civil, palabra_impostor = palabras_funcion(palabras)



    #5. Decir palabras a cada jugador
    #COMENTAR

    PalabrasJugadores(lista_de_jugadores, palabra_civil, palabra_impostor, impostor_jugador)



    #6. Orden de los jugadores y empezar el juego
    #COMENTAR

    lista_orden = orden_jugadores(lista_de_jugadores)

    rondas = comenzar_juego()



    #7. Meter pistas
    #COMENTAR

    lista_pistas = MeterPistas(lista_de_jugadores, rondas)



    #8. Votar
    #COMENTAR

    jugadores = dict(zip(lista_de_jugadores, lista_pistas))

    while True:

        if len(jugadores) > 2:
            eliminado = votacion_ext.votacion(jugadores)

            if EliminarJugador.es_impostor(eliminado, impostor_jugador):

                print(f"{eliminado} es el impostor. Ganan los civiles")
                break

            else:

                print(f"El jugador {eliminado} no era el impostor")
                jugadores.pop(eliminado)
                time.sleep(3)
                clean()

        else:
            print(f"{eliminado} es el impostor. Pierden los civiles")
            input("Presione cualquier tecla para continuar")
            clean()
            break


    if continuar():
        clean()
        continue
    else:
        break

   
