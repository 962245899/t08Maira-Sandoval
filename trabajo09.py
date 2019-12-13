#              10       20         30       40        50        60         70       80        90        100
#    01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="el mayor placer de la vida es hacer lo que la gente dice que no puedes hacer. (walter bagehot)"
#indexacion
print(msg[30]) #impresion de la letra "h"
print(msg[6])  #impresion de la letra "o"
#longitud
print(len("hacer"))      #contabiliza el numero de letras de la palabra "hacer"
print(len("gente"))     #contabiliza el numero de letras de la palabra "gente"
#comparacion
print("vida " != "vida")     #commpara la palabra escrita
#concatenacion
print(msg[48] + msg[0] + msg[12] + msg[0] + msg[69] + msg[23] + msg[92] + msg[62])     #imprimir las palabras "necesito"
#cortado
print(msg[9:15])       #cortar el fragmento"placer"
print(msg[::-1])      #invertir el texto
#iteracion
for de in msg:
    print(de)        #imprimir el texto en vertical
#busqueda
print(msg.count("."))  #numero de "."
print(msg.find("v"))   #lugar de la  primera "v"
print(msg.index("la")) #lugar del primer "la"
