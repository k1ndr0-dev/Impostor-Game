
#Introducir nombres de los jugadores por pantalla
#Capacidad de eliminar jugadores y modificar
#Devuelve una lista de jugadores



def instrucciones():
    print("Introduce el nombre de los jugadores que participan")
    print("En caso de querer cambiar un nombre introduce (1)")
    print("Para finalizar o abandonar el cambio del nombre pulse Intro")


def funcion_lista_jugadores():

    iterador = -1
    jugadores = []

    
    while True:

        iterador += 1
        
        #Introducir nombres
        print("")
        print("Introduce el nombre del jugador ")
        jugadores.append(input().strip()) #.append añade un valor al final de la lista y crea su espacio

        
        #USUARIO INTRODUCE "1"
        #Modificar lista

        if jugadores[iterador] == "1":

            #Eliminamos el "1" introducido ya que está guardado en la lista

            jugadores.pop(iterador) #.pop para eliminar completamente el espacio e información del último dato de la lista

            iterador -= 1 #Decrementamos el iterador para no saltarnos el siguiente espacio de la lista

            #PEDIDA DE DATOS


            print("¿Qué jugador desea modificar?")

            #Imprimir lista de jugadores
            for i in range(0,len(jugadores)):

                print(i+1,". "+jugadores[i])

            
            
            while True:

                #El usuario introduce por teclado un string

                eleccion = input()

                #En caso de darle al Intro, cierra el bucle
                if eleccion == "":

                    break
                

                #En el resto de casos
                else:


                    try:

                        #Intentamos convertir el str introducido a un número entero (int)
                        eleccion = int(eleccion.strip()) #En caso de error, salta a except ValueError



                        #Comprobar si el número introducido está dentro del rango de jugadores introducidos

                        if eleccion < 1 or eleccion > len(jugadores):

                            print(f"Debes de introducir un número dentro del rango de jugadores (1-{len(jugadores)})")



                        else: #En caso de ser un número correcto

                            print("Introduce el nombre del jugador")
                            jugadores[eleccion-1] = input()

                            eleccion = None #Vaciamos los datos que haya introducido el usuario

                            break #Finalizamos el bucle



                    except ValueError: #En caso de ser un dato incorrecto

                        print("Tienes que introducir un número entero")


            

        elif(jugadores[iterador] == ""): 

            jugadores.pop(iterador) #Eliminamos el espacio creado para abandonar el proceso

            return jugadores #Finaliza la función y devuelve la lista de jugadores

