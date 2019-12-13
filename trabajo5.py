#              10       20         30       40        50        60         70
#    012345678901234567890123456789012345678901234567890123456789012345678901
msg="LAS NOTICIAS SON SOLO NOTICIAS, NO HAY MALAS NOTICIAS NI BUENAS NOTICIAS"
#indexacion
print(msg[39]) #impresion de la letra "M"
print(msg[40])  #impresion de la letra "A"
print(msg[41])  #impresion de la letra "L"
print(msg[42])  #impresion de la letra "A"
print(msg[43])  #impresion de la letra "S"

#longitud
print(len("NOTICIAS"))      #contabiliza el numero de letras de la palabra "NOTICIAS"
print(len("BUENAS"))       #contabiliza el numero de letras de la palabra "BUENAS"
#comparacion
print("LAS" == "las")     #commpara la palabra escrita
#concatenacion
print(msg[0] + msg[1] + msg[2] + msg[4] + msg[5] + msg[6] + msg[7] + msg[8] + msg[9]+ msg[10] +msg[11])   #imprimir la palabra "LAS NOTICIAS"
#cortado
print(msg[13:30])       #cortar el fragmento"SON SOLO NOTICIAS"
print(msg[::-1])      #invertir el texto
#iteracion
for NOTICIAS in msg:
    print(NOTICIAS)        #imprimir el texto en vertical
#busqueda
print(msg.count("O")) #numero de "O"
print(msg.find("I")) #lugar de la  primera "I"
print(msg.index("A")) #lugar del primer "A"
