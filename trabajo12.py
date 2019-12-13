#              10
#    0123456789012345
msg="LA VIDA ES SUEÑO"
#indexacion
print(msg[3])  #impresion de la letra "V"
print(msg[4])  #impresion de la letra "I"
print(msg[5])  #impresion de la letra "D"
print(msg[6])  #impresion de la letra "A"

#longitud
print(len("VIDA"))      #contabiliza el numero de letras de la palabra "VIDA"
print(len("SUEÑO"))     #contabiliza el numero de letras de la palabra "SUEÑO"
#comparacion
print("LA" == "la")     #commpara la palabra escrita
#concatenacion
print(msg[0] + msg[1] + msg[3] + msg[4] + msg[5] + msg[6])     #imprimir la palabra "LA VIDA"
#cortado
print(msg[0:26])       #cortar el fragmento"LA VIDA ES SUEÑO"
print(msg[::-1])      #invertir el texto
#iteracion
for VIDA in msg:
    print(VIDA)        #imprimir el texto en vertical
#busqueda
print(msg.count("I")) #numero de "I"
print(msg.find("A")) #lugar de la  primera "A"
print(msg.index("E")) #lugar del primer "E"
