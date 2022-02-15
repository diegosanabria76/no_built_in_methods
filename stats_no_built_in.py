def median(list):
    sum = 0
    counter = 0

    for i in list:
        sum += i
        counter += 1

    median = sum/counter
    return median

def varianza(data):
    #math.sqrt( x - average)2 / n - 1
    n = len(datos)
    nueva_lista = []
    av = average(datos)
    sumatory = 0
    for i in range(len(datos)):
        datos[i] = (datos[i] - av)**2
        nueva_lista.append(datos[i])

    for i in nueva_lista:
        sumatory += i
    varianza = sumatory/ (n-1)
    return varianza
def s_d(variance):
    sd = variance**(1/2)
    return sd

print(median([81,93,98,89,89]))
