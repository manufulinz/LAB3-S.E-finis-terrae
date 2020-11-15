import socket
import primos
import MCD
import random
import Ascii
import Inverso
#Javiera Ruiz
#Manuel Fuentes
#generacion de claves


numeros = primos.pq()

p = numeros[0] #privado
q = numeros[1] #privado
n = p*q #publico
phiN =(p-1)*(q-1)#privado

c=True

while (c):# asegura que el valor de E su mcd con phin sea 1
    
    e=random.randint(2,phiN-1)#publico
    vale=MCD.mcd(e,phiN)
    if (vale==1):
        c=False
    else:
        c=True
    
d=Inverso.modinv(e,phiN)#privado

val=(str(n)+"-"+str(e))

print("Valor e: ",e) 
print("Valor n: ",n)

#Cliente
host = "LocalHost"
port = 5656
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))
print ("Iniciando cliente")
objsocket.send(str(val).encode(encoding ="ascii", errors = "ignore"))

recibido = objsocket.recv(1024)
ap = (recibido.decode(encoding ="ascii",errors ="ignore"))

m= ap.split(",")


texto =[]
for i in range (len(m)):
    if(i==0):
        tempo= str(m[0])
        tempo = tempo.split("[")
        texto.append(int(tempo[1]))
        
        

    elif(i ==(len(m)-1)):

        tempo= str(m[len(m)-1])
        tempo = tempo.split("]")
        texto.append(int(tempo[0]))
        

    else:
        texto.append(int(m[i]))


mense=[]

for i in range(len(texto)):
    encm = int(texto[i])
    f= pow (encm,d,n)
    mense.append(f)
    
        

print("El mensaje cifrado es:",Ascii.ASCII2tex(texto))

mensajefinal= Ascii.ASCII2tex(mense)
print ("El mensaje es: ",mensajefinal)



objsocket.close()
