#              10       20         30       40        50
#    012345678901234567890123456789012345678901234567890123
msg="CUANDO ENTENDERAS QUE MIENTRAS MAS TOMAS, MENOS TIENES"
#indexacion
print(msg[35])  #impresion de la letra "T"
print(msg[36])  #impresion de la letra "O"
print(msg[37])  #impresion de la letra "M"
print(msg[38])  #impresion de la letra "A"
print(msg[39])  #impresion de la letra "S"

#longitud
print(len("MENOS"))      #contabiliza el numero de letras de la palabra "MENOS"
print(len("TIENES"))     #contabiliza el numero de letras de la palabra "TIENES"
#comparacion
print("MAS" == "mas")     #commpara la palabra escrita
#concatenacion
print(msg[7] + msg[8] + msg[9] + msg[10] + msg[11] + msg[12] + msg[13] + msg[14] + msg[15] + msg[16])     #imprimir la palabra "ENTENDERAS"
#cortado
print(msg[0:17])       #cortar el fragmento"CUANDO ENTENDERAS"
print(msg[::-1])      #invertir el texto
#iteracion
for MIENTRAS in msg:
    print(MIENTRAS)        #imprimir el texto en vertical
#busqueda
print(msg.count("A")) #numero de "a"
print(msg.find("M")) #lugar de la  primera "a"
print(msg.index("E")) #lugar del primer "el"
