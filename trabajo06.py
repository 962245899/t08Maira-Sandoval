#              10       20         30       40        50        60         70       80        90
#    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="la sabiduria es un adorno en la prosperidad y un refugio en la adversidad (aristoteles)"
#indexacion
print(msg[32]) #impresion de la letra "p"
print(msg[44])  #impresion de la letra "y"
#longitud
print(len("prosperidad"))      #contabiliza el numero de letras de la palabra "prosperidad"
print(len("y"))     #contabiliza el numero de letras de la palabra "y"
#comparacion
print("en" != "la")     #commpara la palabra escrita
#concatenacion
print(msg[13] + msg[35] + msg[79] + msg[75])     #imprimir las palabras "esta"
#cortado
print(msg[19:25])       #cortar el fragmento"adorno"
print(msg[::-1])      #invertir el texto
#iteracion
for un in msg:
    print(un)        #imprimir el texto en vertical
#busqueda
print(msg.count("v")) #numero de "v"
print(msg.find("v")) #lugar de la  primera "v"
print(msg.index("un")) #lugar del primer "un"
