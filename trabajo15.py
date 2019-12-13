#              10       20         30       40        50        60
#    012345678901234567890123456789012345678901234567890123456789012345678
msg="LA MENTE ES IGUAL QUE UN PARACAIDAS, SOLO FUNCIONA SI SE ABRE"
#indexacion
print(msg[3])  #impresion de la letra "M"
print(msg[4])  #impresion de la letra "E"
print(msg[5])  #impresion de la letra "N"
print(msg[6])  #impresion de la letra "T"
print(msg[7])  #impresion de la letra "E"

#longitud
print(len("MENTE"))      #contabiliza el numero de letras de la palabra "MENTE"
print(len("PARACAIDAS"))     #contabiliza el numero de letras de la palabra "PARACAIDAS"
#comparacion
print("QUE" == "que")     #commpara la palabra escrita
#concatenacion
print(msg[0] + msg[1] + msg[3] + msg[4] + msg[5] + msg[6] + msg[7])     #imprimir la palabra"LA MENTE"
#cortado
print(msg[42:50])       #cortar el fragmento"FUNCIONA"
print(msg[::-1])      #invertir el texto
#iteracion
for FUNCIONA in msg:
    print(FUNCIONA)        #imprimir el texto en vertical
#busqueda
print(msg.count("M")) #numero de "M"
print(msg.find("U")) #lugar de la  primera "U"
print(msg.index("A")) #lugar del primer "A"
