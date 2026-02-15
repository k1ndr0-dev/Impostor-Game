
import unicodedata

def normalizar(texto):

    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto)

    return ''.join(
        c for c in texto
        if unicodedata.category(c) != 'Mn'
    )




def continuar():

    while True:

        seguir = normalizar(input("¿Desea continuar? (Sí/No): "))

        if seguir == "si":
            return True
        elif seguir == "no":
            return False
        else:
            print("Parámetro incorrecto. Debes introducir Sí o No")





      