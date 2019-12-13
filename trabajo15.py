#              10       20         30       40        50        60         70       80        90        100       110
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="no juzgues cada dia por lo que cosechas, sino por las semillas que plantas. (robert louis stevenson)"
#indexacion
print(msg[36]) #impresion de la letra "h"
print(msg[86])  #impresion de la letra "u"
#longitud
print(len("cosechas"))      #contabiliza el numero de letras de la palabra "cosechas"
print(len("plantas"))     #contabiliza el numero de letras de la palabra "plantas"
#comparacion
print("si no" == "sino")     #commpara la palabra escrita
#concatenacion
print(msg[31] + msg[1] + msg[56] + msg[1] + msg[2] + msg[71] + msg[4])     #imprimir las palabras "como tu"
#cortado
print(msg[11:19])       #cortar el fragmento "cada dia"
print(msg[::-1])      #invertir el texto
#iteracion
for por in msg:
    print(por)        #imprimir el texto en vertical
#busqueda
print(msg.count("s"))  #numero de "s"
print(msg.find("a"))   #lugar de la primera "a"
print(msg.index("r")) #lugar del primer "r"
