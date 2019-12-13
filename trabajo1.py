#              10
#    01234567890123456789
msg="SOLO SE QUE NADA SE"
#indexacion
print(msg[0]) #impresion de la letra "s"
print(msg[1])  #impresion de la letra "o"
print(msg[2])  #impresion de la letra "l"
print(msg[3])  #impresion de la letra "o"

#longitud
print(len("SOLO"))      #contabiliza el numero de letras de la palabra "solo"
print(len("SE"))     #contabiliza el numero de letras de la palabra "se"

#comparacion
print("Se" == "se")     #commpara la palabra escrita

#concatenacion
print(msg[0] + msg[1] + msg[2] + msg[3] + msg[5] + msg[6])     #imprimir la palabra "SOLO SE"

#cortado
print(msg[0:3])                  #cortar el fragmento"SOL"
print(msg[19::-1])               #invertir el texto

#iteracion
for SOLO in msg:
    print(SOLO)        #imprimir el texto en vertical

#busqueda
print(msg.count("E")) #numero de "E"
print(msg.find("S")) #lugar de la  primera "S"
print(msg.index("Q")) #lugar del primer "Q"
