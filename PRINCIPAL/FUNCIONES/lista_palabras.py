
import random

palabras = [
    "casa",
    "amigo",
    "comida",
    "escuela",
    "trabajo",
    "familia",
    "tiempo",
    "ciudad",
    "día",
    "noche",
    "agua",
    "música",
    "libro",
    "coche",
    "ropa",
    "teléfono",
    "dinero",
    "calle",
    "sol",
    "amor",
    "Ibai Llanos",
    "Betis",
    "Real Madrid",
    "Árbitro",
    "Hércules de Alicante"
]




def palabras_funcion(palabras):
    palabra_civil = random.choice(palabras)
    palabra_impostor = random.choice(palabras)


    while palabra_impostor == palabra_civil:
        palabra_impostor = random.choice(palabras)
    

    return palabra_civil, palabra_impostor






