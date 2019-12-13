#              10       20         30       40
#    01234567890123456789012345678901234567890123
msg="LOS ABRAZOS SON LA EXPRESION HUMANA DEL ALMA"
#indexacion
print(msg[40])  #impresion de la letra "A"
print(msg[41])  #impresion de la letra "L"
print(msg[42])  #impresion de la letra "M"
print(msg[43])  #impresion de la letra "A"

#longitud
print(len("ABRAZOS"))      #contabiliza el numero de letras de la palabra "ABRAZOS"
print(len("HUMANA"))     #contabiliza el numero de letras de la palabra "HUMANA"
#comparacion
print("LA" == "la")     #commpara la palabra escrita
#concatenacion
print(msg[19] + msg[20] + msg[21] + msg[22] + msg[23] + msg[24] + msg[25] + msg[26] + msg[27])     #imprimir la palabra "EXPRESION"
#cortado
print(msg[29:35])       #cortar el fragmento"EXPRESION HUMANA"
print(msg[::-1])      #invertir el texto
#iteracion
for EXPRESION in msg:
    print(EXPRESION)        #imprimir el texto en vertical
#busqueda
print(msg.count("I")) #numero de "I"
print(msg.find("O")) #lugar de la  primera "O"
print(msg.index("U")) #lugar del primer "U"
