

def es_impostor(jugador_eliminado: list,impostor: str) -> bool:

    if next(iter(jugador_eliminado)) == impostor:

        return True
    else:

        return False
    




