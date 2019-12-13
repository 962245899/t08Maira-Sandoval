#              10       20         30       40        50        60         70
#    01234567890123456789012345678901234567890123456789012345678901234567890
msg="el verdadero discipulo es el que supera al maestro (aristoteles)"
#indexacion
print(msg[14]) #impresion de la letra "i"
print(msg[51])  #impresion del signo "("
#longitud
print(len("discipulo"))      #contabiliza el numero de letras de la palabra "discipulo"
print(len("aristoteles"))     #contabiliza el numero de letras de la palabra "aristoteles"
#comparacion
print("maestro" == "aristoteles")     #commpara la palabra escrita
#concatenacion
print(msg[7] + msg[12] + msg[27] + msg[44])     #imprimir las palabras "a la"
#cortado
print(msg[33:50])       #cortar el fragmento"supera al maestro"
print(msg[::-1])      #invertir el texto
#iteracion
for el in msg:
    print(el)        #imprimir el texto en vertical
#busqueda
print(msg.count("e")) #numero de "e"
print(msg.find("d")) #lugar de la  primera "d"
print(msg.index("el")) #lugar del primer "el"
