#              10       20         30       40        50        60         70       80        90        100
#    01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="¡Nunca te rindas! El fracaso y el rechazo son solo el primer escalon hacia el exito (jim valvano)"
#indexacion
print(msg[26]) #impresion de la letra "s"
print(msg[0])  #impresion de la letra "i"
#longitud
print(len("solo"))      #contabiliza el numero de letras de la palabra "solo"
print(len("exito"))     #contabiliza el numero de letras de la palabra "exito"
#comparacion
print("El" == "el")     #commpara la palabra escrita
#concatenacion
print(msg[18] + msg[32] + msg[41] + msg[57] + msg[8] + msg[85] + msg[27] + msg[10])     #imprimir la palabra "El mejor"
#cortado
print(msg[:17])       #cortar el fragmento"!nunca te rindas!"
print(msg[::-1])      #invertir el texto
#iteracion
for exito in msg:
    print(exito)        #imprimir el texto en vertical
#busqueda
print(msg.count("a")) #numero de "a"
print(msg.find("a")) #lugar de la  primera "a"
print(msg.index("el")) #lugar del primer "el"
