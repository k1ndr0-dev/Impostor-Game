

def renombrar_repetidos(lista: list) -> list:

    contador = {}      # Para contar cuántas veces aparece cada nombre
    resultado = []     # Nueva lista con los nombres modificados

    for nombre in lista:

        if nombre not in contador:

            contador[nombre] = 1
            resultado.append(nombre)

        else:

            contador[nombre] += 1
            resultado.append(f"{nombre}{contador[nombre]}")

    return resultado



