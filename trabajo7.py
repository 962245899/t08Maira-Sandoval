#              10       20         30       40        50        60
#    012345678901234567890123456789012345678901234567890123456789012345678
msg="JAMAS CUMPLIRAS CON SU DESTINO HASTA QUE DEJES LA ILUSION DEL CONTROL"
#indexacion
print(msg[0])  #impresion de la letra "J"
print(msg[1])  #impresion de la letra "A"
print(msg[2])  #impresion de la letra "M"
print(msg[3])  #impresion de la letra "A"
print(msg[4])  #impresion de la letra "S"

#longitud
print(len("ILUSION"))      #contabiliza el numero de letras de la palabra "ILUSION"
print(len("CONTROL"))     #contabiliza el numero de letras de la palabra "CONTROL"
#comparacion
print("LA" == "la")     #commpara la palabra escrita
#concatenacion
print(msg[6] + msg[7] + msg[8] + msg[9] + msg[10] + msg[11] + msg[12] + msg[13] + msg[14])     #imprimir la palabra "CUMPLIRAS"
#cortado
print(msg[0:15])       #cortar el fragmento"JAMAS CUMPLIRAS"
print(msg[::-1])      #invertir el texto
#iteracion
for ILUSION in msg:
    print(ILUSION)        #imprimir el texto en vertical
#busqueda
print(msg.count("I")) #numero de "I"
print(msg.find("O")) #lugar de la  primera "O"
print(msg.index("U")) #lugar del primer "U"
