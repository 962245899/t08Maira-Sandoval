#              10       20         30       40
#    0123456789012345678901234567890123456789012345678
msg="LA RISA ES LA MEDICINA PARA EL DOLOR MAS EFECTIVA"
#indexacion
print(msg[3])  #impresion de la letra "R"
print(msg[4])  #impresion de la letra "I"
print(msg[5])  #impresion de la letra "S"
print(msg[6])  #impresion de la letra "A"

#longitud
print(len("MEDICINA"))      #contabiliza el numero de letras de la palabra "MEDICINA"
print(len("DOLOR"))     #contabiliza el numero de letras de la palabra "DOLOR"
#comparacion
print("LA" == "la")     #commpara la palabra escrita
#concatenacion
print(msg[41] + msg[42] + msg[43] + msg[44] + msg[45] + msg[46] + msg[47] + msg[48])     #imprimir la palabra "EFECTIVA"
#cortado
print(msg[0:7])       #cortar el fragmento"LA RISA"
print(msg[::-1])      #invertir el texto
#iteracion
for RISA in msg:
    print(RISA)        #imprimir el texto en vertical
#busqueda
print(msg.count("R")) #numero de "R"
print(msg.find("M")) #lugar de la  primera "M"
print(msg.index("A")) #lugar del primer "A"
