#              10       20         30       40        50        60         70
#    01234567890123456789012345678901234567890123456789012345678901234567890
msg="saber y saberlo demostrar es valer dos veces (baltasar gracian)"
#indexacion
print(msg[37]) #impresion de la letra "s"
print(msg[35])  #impresion de la letra "d"
#longitud
print(len("demostrar"))      #contabiliza el numero de letras de la palabra "demostrar"
print(len("saberlo"))     #contabiliza el numero de letras de la palabra "saberlo"
#comparacion
print(" valer" == "valer")     #commpara la palabra escrita
#concatenacion
print(msg[41] + msg[1] + msg[12] + msg[55] + msg[23] + msg[12])     #imprimir la palabra "cargar"
#cortado
print(msg[16:44])       #cortar el fragmento"demostrar es valer dos veces"
print(msg[::-1])      #invertir el texto
#iteracion
for es in msg:
    print(es)        #imprimir el texto en vertical
#busqueda
print(msg.count("i")) #numero de "i"
print(msg.find("r")) #lugar de la  primera "r"
print(msg.index("es")) #lugar del primer "es"
