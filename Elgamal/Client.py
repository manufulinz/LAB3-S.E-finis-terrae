import socket
import Ascii
import GenAp
import random
#Javiera Ruiz
#Manuel Fuentes

#generacion de claves

respuestas = []
numeros = GenAp.AP()

p = numeros[0] #publico
g = numeros[1] #publico
a = random.randint(2,p-1) #privado
K = pow(g,a)%p #publico
clave = (str(p)+"-"+str(g)+"-"+str(K))
print("Valor P: ",p)
print("Valor G: ",g)
print("Valor K: ",K)

#Cliente
host = "LocalHost"
port = 5656
objsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host, port))
print ("Iniciando cliente")
objsocket.send(clave.encode(encoding ="ascii", errors = "ignore"))

recibido = objsocket.recv(1024)
ap = (recibido.decode(encoding ="ascii",errors ="ignore"))
val = ap.split("-")
y1 = val[0]
y2 = val[1]
y2 = y2.split(sep=",")

y1 = int(y1)

texto = Ascii.Text2ASCII(str(y2))


texto =[]
for i in range (len(y2)):
    if(i==0):
        tempo= str(y2[0])
        tempo = tempo.split("[")
        texto.append(int(tempo[1]))
        
        

    elif(i ==(len(y2)-1)):

        tempo= str(y2[len(y2)-1])
        tempo = tempo.split("]")
        texto.append(int(tempo[0]))
        

    else:
        texto.append(int(y2[i]))

mense=[]
for i in range(len(texto)):
    y2 = int(texto[i])
    m = (y1**(p-1-a)*y2)%p
    mense.append(m)
    
        

print("El mensaje cifrado es:",Ascii.ASCII2tex(texto))

mensajefinal= Ascii.ASCII2tex(mense)
print ("El mensaje es: ",mensajefinal)



objsocket.close()
