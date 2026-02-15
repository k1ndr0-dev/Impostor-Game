from .BorrarPantalla import clean

def PalabrasJugadores(lista_de_jugadores, palabra_civil, palabra_impostor, impostor_jugador):
    
    for jugador in lista_de_jugadores:

        if jugador == impostor_jugador:
            print(f"Es el turno de {jugador}")
            input("Pulsa ENTER para ver tu palabra...")
            print("ERES EL IMPOSTOR")
            input(f"Tu palabra es: {palabra_impostor}\n\nPulsa ENTER para continuar...")
            clean()


        else:

            print(f"Es el turno de {jugador}")
            input("Pulsa ENTER para ver tu palabra...")
            print("ERES CIVIL")
            input(f"Tu palabra es: {palabra_civil}\n\nPulsa ENTER para continuar...")
            clean()



