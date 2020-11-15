import socket
import primos
import MCD
import random
import Ascii
import Inverso

texto= open("mensajeentrada.txt","r")
mensaje= texto.read()
texto.close()
m = Ascii.Text2ASCII(mensaje)
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

ap = respuestas[0]
ap = ap.split("-")
n = int(ap[0])
e = int(ap[1])

print("Valor e: ",e)
print("Valor n: ",n)

#Cifrar
tex = []

for i in range(len(m)):
    enc = m[i]**e%n
    tex.append(enc)
   
activeConection.send(str(tex).encode(encoding = "ascii", errors="ignore"))
textoc = Ascii.ASCII2tex(tex)
print("Mensaje: ",textoc)

'''
activeConection, addr = server.accept()
recibido = activeConection.recv(1024)
respuestas.append(recibido.decode(encoding = "ascii", errors="ignore"))
print (respuestas)

c =0
ap = respuestas[0]
ap = ap.split("-")
p = int(ap[0])
g = int(ap[1])
K = int(ap[2])
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

    
    
activeConection.close()'''
