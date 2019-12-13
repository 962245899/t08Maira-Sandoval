#              10       20         30       40        50        60         70       80        90
#    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="apunta a la luna. si fallas, podrias dar a una estrella. (w. clement stone)"
#indexacion
print(msg[16]) #impresion del signo "."
print(msg[6])  #impresion del "espacio"
#longitud
print(len("clement"))      #contabiliza el numero de letras de la palabra "clement"
print(len("estrella"))     #contabiliza el numero de letras de la palabra "estrella"
#comparacion
print("a la" != "a una")     #commpara la palabra escrita
#concatenacion
print(msg[18] + msg[30] + msg[12] + msg[30] + msg[6] + msg[4] + msg[2] + msg[16])     #imprimir las palabras "solo tu."
#cortado
print(msg[21:27])       #cortar el fragmento"fallas"
print(msg[::-1])      #invertir el texto
#iteracion
for a in msg:
    print(a)        #imprimir el texto en vertical
#busqueda
print(msg.count("l"))  #numero de "l"
print(msg.find("a"))   #lugar de la  primera "a"
print(msg.index("si")) #lugar del primer "si"
