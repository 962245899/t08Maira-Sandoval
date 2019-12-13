#              10       20         30       40        50        60         70       80        90        100       110
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="vive como si fueses a morir mañana. aprende como si fueses a vivir para siempre. (mahatma gandhi)"
#indexacion
print(msg[30]) #impresion de la letra "ñ"
print(msg[84])  #impresion de la letra "h"
#longitud
print(len("mañana"))      #contabiliza el numero de letras de la palabra "mañana"
print(len("siempre"))     #contabiliza el numero de letras de la palabra "siempre"
#comparacion
print("a" == "a")     #commpara la palabra escrita
#concatenacion
print(msg[90] + msg[24] + msg[29] + msg[32] + msg[93] + msg[3])     #imprimir las palabras "grande"
#cortado
print(msg[61:79])       #cortar el fragmento"vivir para siempre"
print(msg[::-1])      #invertir el texto
#iteracion
for a in msg:
    print(a)        #imprimir el texto en vertical
#busqueda
print(msg.count("h"))  #numero de "h"
print(msg.find("f"))   #lugar de la primera "f"
print(msg.index("a")) #lugar del primer "a"
