#              10       20         30       40        50        60         70       80        90        100       110
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="para tener exito, tus deseos de triunfar deberian ser mas grandes que tu miedo de fracasar. (bill cosby)"
#indexacion
print(msg[90]) #impresion del "."
print(msg[16])  #impresion del ","
#longitud
print(len("deseos"))      #contabiliza el numero de letras de la palabra "deseos"
print(len("triunfar"))     #contabiliza el numero de letras de la palabra "triunfar"
#comparacion
print("tus" != "tu")     #commpara la palabra escrita
#concatenacion
print(msg[7] + msg[15] + msg[4] + msg[82] + msg[83]+ msg[84] + msg[85] + msg[86] + msg[87] + msg[88] + msg[89])   #imprimir las palabras "no fracasar"
#cortado
print(msg[58:65])       #cortar el fragmento"grandes"
print(msg[::-1])      #invertir el texto
#iteracion
for tu in msg:
    print(tu)        #imprimir el texto en vertical
#busqueda
print(msg.count("t"))  #numero de "t"
print(msg.find("d"))   #lugar de la primera "d"
print(msg.index("b")) #lugar del primer "b"
