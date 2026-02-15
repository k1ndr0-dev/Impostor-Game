from .CivilesImpostor import impostor
from .lista_palabras import palabras_funcion
from .EsperarTecla import EsperarTecla
from .nombres import funcion_lista_jugadores



def PalabrasJugadores(impostor_jugador, jugadores):

    palabra_impostor, palabra_civil = palabras_funcion()

    for jugador in jugadores:

        if jugador == impostor_jugador:

            print(f"Es el turno de {jugador}")
            EsperarTecla()
            print(f"Eres impostor. Tu palabra es: {palabra_impostor}")
            EsperarTecla()

        else:

            print(f"Es el turno de {jugador}")
            EsperarTecla()
            print(f"Eres civil. Tu palabra es: {palabra_civil}")
            EsperarTecla()
    



