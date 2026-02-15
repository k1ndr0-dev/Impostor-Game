from .BorrarPantalla import clean


def MeterPistas(lista_jugadores, rondas):

    lista_pistas = [[ None for _ in range(rondas)] for _ in range(len(lista_jugadores))]

    x = -1
    y = 0

    for i in range (1, ( ( len(lista_jugadores) ) * rondas) + 1):

        if (i >= len(lista_jugadores)):

            if (i % len(lista_jugadores) == 1):

                x = 0
                y += 1

            else:

                x += 1

        else:

            x += 1

        print(f"Es el turno de: {lista_jugadores[x]}")

        lista_pistas[x][y] = input("Introduce tu pista: ")
        clean()

    return lista_pistas


