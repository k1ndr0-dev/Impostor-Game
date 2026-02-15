

def imprimir(diccionario: dict):

    texto = ""
    contador = 0

    for jugador, pistas in diccionario.items():

        contador += 1

        texto += f"{contador}.{jugador}:\n"

        for pista in pistas:
            texto += f"- {pista}\n"

    print(texto)
        


