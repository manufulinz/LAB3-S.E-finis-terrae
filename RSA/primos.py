
import random
def pq():
    primos = [2]
    nmax = 1000
    for x in range(3, nmax):
        for i in range(2, x):
            if x%i != 0:
                #i no es divisor de x, x puede ser primo
                continue
            else:
                #i es divisor de x, x no es primo
                break #No es necesario buscar más divisores
        else:
            #El bucle for ha terminado con normalidad
            #El número que estábamos comprobando es primo
            primos.append(x)
    F = open('numerosprimos.txt', 'w')
    p = (random.choice(primos))
    q = (random.choice(primos))
    pq =[p,q]
    return pq
