#              10
#    01234567890123456
msg="¡NUNCA TE RINDAS!"
#indexacion
print(msg[1]) #impresion de la letra "N"
print(msg[2])  #impresion de la letra "U"
print(msg[3])  #impresion de la letra "N"
print(msg[4])  #impresion de la letra "C"
print(msg[5])  #impresion de la letra "A"

#longitud
print(len("NUNCA TE RINDAS"))      #contabiliza el numero de letras de la palabra "NUNCA TE RINDAS"

#comparacion
print("TE" == "te")     #commpara la palabra escrita
#concatenacion
print(msg[10] + msg[11] + msg[12] + msg[13] + msg[14] + msg[15])     #imprimir la palabra "RINDAS"
#cortado
print(msg[:17])       #cortar el fragmento"!NUNCA TE RINDAS!"
print(msg[::-1])      #invertir el texto
#iteracion
for NUNCA in msg:
    print(NUNCA)        #imprimir el texto en vertical
#busqueda
print(msg.count("U")) #numero de "U"
print(msg.find("A")) #lugar de la  primera "A"
print(msg.index("I")) #lugar del primer "I"
