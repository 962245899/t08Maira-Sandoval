#              10       20         30       40        50        60         70       80        90        100      110
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="un pueblo sin el conocimiento de su historia, origen y la cultura es como un arbol sin raices. (marcus garvey)"
#indexacion
print(msg[36]) #impresion de la letra "h"
print(msg[44])  #impresion del ","
#longitud
print(len("pueblo"))      #contabiliza el numero de letras de la palabra "pueblo"
print(len("conocimiento"))     #contabiliza el numero de letras de la palabra "conocimiento"
#comparacion
print("un" != "un")     #commpara la palabra escrita
#concatenacion
print(msg[3] + msg[43] + msg[41] + msg[77])     #imprimir las palabras "para"
#cortado
print(msg[36:44])       #cortar el fragmento"historia"
print(msg[::-1])      #invertir el texto
#iteracion
for el in msg:
    print(el)        #imprimir el texto en vertical
#busqueda
print(msg.count("u"))  #numero de "u"
print(msg.find("c"))   #lugar de la primera "c"
print(msg.index("h")) #lugar del primer "h"
