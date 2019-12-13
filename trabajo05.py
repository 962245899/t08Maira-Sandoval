#              10       20         30       40        50        60         70
#    01234567890123456789012345678901234567890123456789012345678901234567890
msg="daria todo lo que se, por la mitad de lo que ignoro (rene descartes)"
#indexacion
print(msg[39]) #impresion de la letra "o"
print(msg[20])  #impresion del signo ","
#longitud
print(len("descartes"))      #contabiliza el numero de letras de la palabra "descartes"
print(len("se"))     #contabiliza el numero de letras de la palabra "se"
#comparacion
print("descartes" != "rene")     #commpara la palabra escrita
#concatenacion
print(msg[61] + msg[4] + msg[29] + msg[32])     #imprimir las palabras "cama"
#cortado
print(msg[29:34])       #cortar el fragmento"mitad"
print(msg[::-1])      #invertir el texto
#iteracion
for de in msg:
    print(de)        #imprimir el texto en vertical
#busqueda
print(msg.count("l")) #numero de "l"
print(msg.find("e")) #lugar de la  primera "e"
print(msg.index("lo")) #lugar del primer "lo"
