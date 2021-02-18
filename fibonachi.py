import pandas
import numpy
from pandas import Series, DataFrame
import fibonacci

# verifica si el numero ingresado es pan digital
def EsPanDigital(numero):
    for i in range(1,9):
        if str(i) in numero :
            continue
        else :
            return False
    return True
# busca apartir del primer numero con pan digital de los primeros 9 digitos 
# el numero que tenga pan digital en los primeros y en los ultimos numeros     
def CalculcarPanDigitalDoble():
    count = 2750 # la respuesta del problema es 329468
    while True:
        numeroEvaluar = str(fibonacci.fibo(count))
        panDigitalI = numeroEvaluar[:9]
        panDigitalD = numeroEvaluar[len(numeroEvaluar)-9:]
        if EsPanDigital(panDigitalI) and EsPanDigital(panDigitalD):
            return  numeroEvaluar
        else:
            count+=1
            print(count)
            continue   



print ("el pan digital doble de la serie de fibonachi es : \n" + str(CalculcarPanDigitalDoble()) )





