#              10       20         30       40        50        60
#    0123456789012345678901234567890123456789012345678901234567890123
msg="UNO SUELE HALLAR SU DESTINO EN EL SENDERO QUE TOMA PARA EVITARLO"
#indexacion
print(msg[10])  #impresion de la letra "H"
print(msg[11])  #impresion de la letra "A"
print(msg[12])  #impresion de la letra "L"
print(msg[13])  #impresion de la letra "L"
print(msg[14])  #impresion de la letra "A"
print(msg[15])  #impresion de la letra "R"

#longitud
print(len("SUELE"))      #contabiliza el numero de letras de la palabra "SUELE"
print(len("HALLAR"))     #contabiliza el numero de letras de la palabra "HALLAR"
#comparacion
print("SU" == "su")     #commpara la palabra escrita
#concatenacion
print(msg[20] + msg[21] + msg[22] + msg[23] + msg[24] + msg[25] + msg[26])     #imprimir la palabra "SENDERO"
#cortado
print(msg[56:64])       #cortar el fragmento"EVITARLO"
print(msg[::-1])      #invertir el texto
#iteracion
for HALLAR in msg:
    print(HALLAR)        #imprimir el texto en vertical
#busqueda
print(msg.count("A")) #numero de "A"
print(msg.find("R"))  #lugar de la  primera "R"
print(msg.index("U")) #lugar del primer "U"
