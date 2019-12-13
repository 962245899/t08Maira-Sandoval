#              10       20         30       40
#    0123456789012345678901234567890123456789012345678
msg="EL CORAZON ES EL UNICO QUE AUN DESTROZADO TRABAJA"
#indexacion
print(msg[17])  #impresion de la letra "U"
print(msg[18])  #impresion de la letra "N"
print(msg[19])  #impresion de la letra "I"
print(msg[20])  #impresion de la letra "C"
print(msg[21])  #impresion de la letra "O"

#longitud
print(len("CORAZON"))      #contabiliza el numero de letras de la palabra "CORAZON"
print(len("DESTROZADO"))     #contabiliza el numero de letras de la palabra "DESTROZADO"
#comparacion
print("ES" == "es")     #commpara la palabra escrita
#concatenacion
print(msg[42] + msg[43] + msg[44] + msg[45] + msg[46] + msg[47] + msg[48])     #imprimir la palabra "TRABAJA"
#cortado
print(msg[0:10])       #cortar el fragmento"EL CORAZON"
print(msg[::-1])      #invertir el texto
#iteracion
for TRABAJA in msg:
    print(TRABAJA)        #imprimir el texto en vertical
#busqueda
print(msg.count("A")) #numero de "A"
print(msg.find("O"))  #lugar de la  primera "O"
print(msg.index("N")) #lugar del primer "N"
