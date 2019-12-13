#              10       20         30       40        50        60        70        80        90       100
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901
msg="AHORA SOY CONSCIENTE QUE HAY CAMINOS QUE ACABAN EN OTROS Y HAY PERSONAS QUE ACABAN EN OTRAS POR QUE SI"
#indexacion
print(msg[29])  #impresion de la letra "C"
print(msg[30])  #impresion de la letra "A"
print(msg[31])  #impresion de la letra "M"
print(msg[32])  #impresion de la letra "I"
print(msg[33])  #impresion de la letra "N"
print(msg[34])  #impresion de la letra "O"
print(msg[35])  #impresion de la letra "S"


#longitud
print(len("CONSCIENTE"))      #contabiliza el numero de letras de la palabra "CONSCIENTE"
print(len("OTROS"))     #contabiliza el numero de letras de la palabra "OTROS"
#comparacion
print("SOY" == "soy")     #commpara la palabra escrita
#concatenacion
print(msg[63] + msg[64] + msg[65] + msg[66] + msg[67] + msg[68] + msg[69] + msg[70])     #imprimir la palabra "PERSONAS"
#cortado
print(msg[41:47])       #cortar el fragmento"JAMAS CUMPLIRAS"
print(msg[::-1])      #invertir el texto
#iteracion
for PERSONAS in msg:
    print(PERSONAS)        #imprimir el texto en vertical
#busqueda
print(msg.count("E")) #numero de "E"
print(msg.find("R")) #lugar de la  primera "R"
print(msg.index("A")) #lugar del primer "A"
