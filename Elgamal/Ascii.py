def Text2ASCII(Cadena):
    i = 0 					           # Variable del bucle.
    Size = len(Cadena)		     # Longitud de la cadena.
    Temp = []					        # Variable temporal, donde se construirá la cadena en ASCII.
    while i < Size:  				      # Instancia del bucle.
        Temp.append(ord(Cadena[i])) # Se empieza a contruir la palabra, usando la función ord().
        i += 1 					      # Aumentamos el valor de la variable del bucle.
    return Temp

def ASCII2tex(Cadena):					          
    Temp = []
    i = 0
    Size = len(Cadena)
    while i < Size: 
        Temp.append(chr(Cadena[i]))
        i += 1

    Temp ="".join(Temp)
    return Temp
