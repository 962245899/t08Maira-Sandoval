#              10       20         30       40        50        60         70       80
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="las raices de la educacion son amargas, pero el fruto es dulce (aristoteles)"
#indexacion
print(msg[35]) #impresion de la letra "g"
print(msg[48])  #impresion de la letra "f"
#longitud
print(len("educacion"))      #contabiliza el numero de letras de la palabra "educacion"
print(len("raices"))     #contabiliza el numero de letras de la palabra "raices"
#comparacion
print("aristoteles" != "aristoteles")     #commpara la palabra escrita
#concatenacion
print(msg[51] + msg[5] + msg[34] + msg[18] + msg[45])     #imprimir las palabras "tarde"
#cortado
print(msg[31:38])       #cortar el fragmento"amargas"
print(msg[::-1])      #invertir el texto
#iteracion
for la in msg:
    print(la)        #imprimir el texto en vertical
#busqueda
print(msg.count("e"))  #numero de "e"
print(msg.find("g"))   #lugar de la  primera "g"
print(msg.index("de")) #lugar del primer "de"
