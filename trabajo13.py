#              10       20         30       40        50        60         70
#    01234567890123456789012345678901234567890123456789012345678901234567890
msg="si crees que puedes o crees que no puedes tienes razon. (henry ford)"
#indexacion
print(msg[51]) #impresion de la letra "z"
print(msg[61])  #impresion de la letra "y"
#longitud
print(len("razon"))      #contabiliza el numero de letras de la palabra "razon"
print(len("henry"))     #contabiliza el numero de letras de la palabra "henry"
#comparacion
print("que" != "que ")     #commpara la palabra escrita
#concatenacion
print(msg[61] + msg[2] + msg[0] + msg[5] + msg[4])     #imprimir las palabras "y ser"
#cortado
print(msg[49:54])       #cortar el fragmento"razon"
print(msg[::-1])      #invertir el texto
#iteracion
for que in msg:
    print(que)        #imprimir el texto en vertical

#busqueda
print(msg.count("s"))  #numero de "s"
print(msg.find("o"))   #lugar de la primera "o"
print(msg.index("c")) #lugar del primer "c"
