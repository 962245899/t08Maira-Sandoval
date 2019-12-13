#              10       20         30       40        50        60
#    0123456789012345678901234567890123456789012345678901234567890123456
msg="¡LLORA! NO TE AVERGUENZES DE CONFESAR DE QUE ME HAS QUERIDO UN POCO"
#indexacion
print(msg[1])  #impresion de la letra "L"
print(msg[2])  #impresion de la letra "L"
print(msg[3])  #impresion de la letra "O"
print(msg[4])  #impresion de la letra "R"
print(msg[5])  #impresion de la letra "A"

#longitud
print(len("¡LLORA!"))      #contabiliza el numero de letras de la palabra "¡LLORA!"
print(len("CONFESAR"))     #contabiliza el numero de letras de la palabra "CONFESAR"
#comparacion
print("NO" == "no")     #commpara la palabra escrita
#concatenacion
print(msg[52] + msg[53] + msg[54] + msg[55] + msg[56] + msg[57] + msg[58])     #imprimir la palabra "QUERIDO"
#cortado
print(msg[8:25])       #cortar el fragmento"NO TE AVERGUENZES"
print(msg[::-1])      #invertir el texto
#iteracion
for CONFESAR in msg:
    print(CONFESAR)        #imprimir el texto en vertical
#busqueda
print(msg.count("A")) #numero de "A"
print(msg.find("O")) #lugar de la  primera "O"
print(msg.index("R")) #lugar del primer "R"
