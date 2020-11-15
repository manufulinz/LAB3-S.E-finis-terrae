import socket
import GenAp
import random
import Ascii
#Javiera Ruiz
#Manuel Fuentes

texto= open("mensajeentrada.txt","r")
mensaje= texto.read()
texto.close()
mensajeas = Ascii.Text2ASCII(mensaje)

#Servidor
respuestas = []
host = "LocalHost"
port = 5656
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server en espera de conexiones")


activeConection, addr = server.accept()
recibido = activeConection.recv(1024)
respuestas.append(recibido.decode(encoding = "ascii", errors="ignore"))


c =0
ap = respuestas[0]
ap = ap.split("-")
p = int(ap[0])
g = int(ap[1])
K = int(ap[2])
#numero privado
b = random.randint(2, p-10)

print("Valor P: ",p)
print("Valor G: ",g)
print("Valor K: ",K)

y1 = pow(g,b)%p
cifrado= []
print ("El valor y1 es: ",y1)
for i in range (0, len(mensajeas)):
    temp = mensajeas[i]
    y2 = pow(K,b)*temp %p
    cifrado.append(int(y2))
print("El valor m es: ", Ascii.ASCII2tex(cifrado))

en = (str(y1)+"-"+str(cifrado))

enviar=str (en)
activeConection.send(enviar.encode(encoding = "ascii", errors="ignore"))

    
    
activeConection.close() 
