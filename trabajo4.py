#              10       20
#    0123456789012345678901234
msg="LOS ACCIDENTES NO EXISTEN"
#indexacion
print(msg[18]) #impresion de la letra  "E"
print(msg[19])  #impresion de la letra "X"
print(msg[20])  #impresion de la letra "I"
print(msg[21])  #impresion de la letra "S"
print(msg[22])  #impresion de la letra "T"
print(msg[23])  #impresion de la letra "E"
print(msg[24])  #impresion de la letra "N"

#longitud
print(len("EXISTEN"))      #contabiliza el numero de letras de la palabra "EXISTEN"
print(len("ACCIDENTES"))     #contabiliza el numero de letras de la palabra "ACCIDENTES"
#comparacion
print("LOS" == "los")     #commpara la palabra escrita
#concatenacion
print(msg[0] + msg[1] + msg[2] + msg[4] + msg[5] + msg[6] + msg[7] + msg[8] + msg[9] + msg[10] + msg[11] + msg[12] + msg[13])     #imprimir la palabra "LOS ACCIDENTES"
#cortado
print(msg[15:25])       #cortar el fragmento"NO EXISTEN"
print(msg[::-1])      #invertir el texto
#iteracion
for EXISTEN in msg:
    print(EXISTEN)        #imprimir el texto en vertical
#busqueda
print(msg.count("E")) #numero de "E"
print(msg.find("I"))   #lugar de la  primera "I"
print(msg.index("S")) #lugar del primer "S"
