# Enunciado 
# Ana, José y Juan, se fueron una tarde a jugar ping-pong, cada uno jugó la siguiente
#cantidad de partidos. Cada que un jugador pierde una partida arranca otra con el jugador en
#espera. Ejemplo: Ana vs Juan (Ana gana) - juega (Ana vs Juan), el ganador siempre juega
#contra el jugador que está en espera y así sucesivamente hasta completar el número de
#partidas que se muestran a continuación.
#Basado en los datos de los partidos jugados realizar lo siguiente:
#● ¿Quién perdió el segundo partido?
#Liste el resultado del primer punto y los partidos perdidos en el orden correcto, en un JSON.


# Respuesta
# dado que por cada partida hay dos jugadores, si sumamos todas las partidas jugadas por cada uno estariamos contando doble cada partida
# ejemplo, si ana jugo contra jose, esa unica partida esta contada dentro de las partidas de ana y las de jose por lo q se contaria doble 
# por lo que al sumar las partidas tenemos 42 pero dado que estan contadas dobles el resultado real de partidas jugadas es 21 

# Comprobacion mediante ecuaciones 
# si planteamos la suma de las partidas que juan tuvo con ana y con jose deberia dar 10, segun la informacion del enunciado
#J = Juan
#A = Ana
#S = Jose
#  JA + JS = 10
#  JA + AS = 17
# AS + JS = 15
# solucionando el sistema de ecuaciones tenemos que JA = 6,  JS = 4 y AS = 11 
# sumando el total de las partidas tenemos que se jugaron 21 

# para deducir quien perdio la segunda partida , primero debemos analizar el peor de los casos de un jugador
# el minimo de partidas jugadas dado que las haya perdido todas
# teniendo en cuenta que dos partidas consecutivas los 3 jugadores juegan al menos 1 partida, y si se pierden todas se jugaria alternadamente, (pierdo descanzo, pierdo descanzo) el minimo de partidas jugadas perdiendo todas las partidas seria 11 si arranco a jugar en la primera partida y 10 si arranca desde la segunda. Dado que el minimo de partidas jugadas seria 10 significa que la unica manera de que juan solo haya jugado 10 partidas es que las perdio todas y arranco a jugar en la segunda partida, por lo q se deduce que el jugador que perdio la segunda partida es juan

import json
# metodo que calcula las partidas totales jugadas por los 3 jugadores 
def calcularPartidas(partidasXjugadorTotales, numeroOponentes):
    return (partidasXjugadorTotales / numeroOponentes)

partidas_ana = 17
partidas_jose = 15
partidas_juan = 10

# metodo que calcula las partidas minimas jugadas por un jugador
def calcularPartidasMinimas3Jugadores(partidasNetas):
    if numeroIntercalados(partidasNetas, 2) > numeroIntercalados(partidasNetas, 3):
        return numeroIntercalados(partidasNetas, 3)
    else:
        return numeroIntercalados(partidasNetas, 2)

# metodo que calcula el numero de partidas jugadas asumiendo que se pierden todas (siempre que juego, salgo)
def numeroIntercalados(numero, modulo):
    count = 0.0
    for i in range(1,numero):
        if modulo == 2 :
            if i%2 == 0 :
                count+=1
        else:
            if i%2 != 0 :
                count+=1
     return count

suma = partidas_juan + partidas_jose + partidas_ana
total = calcularPartidas(suma, 2)
print("total es igual a " + str(total))

print("partidas minimas jugables :" + str(calcularPartidasMinimas3Jugadores(int(total))))
resultado = {"JugadorPerdedorSegundoJuego": "Juan", "partidas perdidas": [i for i in range(1,int(total)) if i%2==0]}
json_dump = json.dumps(resultado)
print("Hello world")
print (json_dump)