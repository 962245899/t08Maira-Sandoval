#              10       20         30       40        50        60         70
#    01234567890123456789012345678901234567890123456789012345678901234567890
msg="cada logro comienza con la decision de intentarlo. (gail devers)"
#indexacion
print(msg[46]) #impresion de la letra "r"
print(msg[5])  #impresion dela letra "l"
#longitud
print(len("comienza"))      #contabiliza el numero de letras de la palabra "comienza"
print(len("devers"))     #contabiliza el numero de letras de la palabra "devers"
#comparacion
print("conla " != "con la")     #commpara la palabra escrita
#concatenacion
print(msg[16] + msg[6] + msg[41] + msg[53])     #imprimir las palabras "nota"
#cortado
print(msg[39:49])       #cortar el fragmento"intentarlo"
print(msg[::-1])      #invertir el texto
#iteracion
for la in msg:
    print(la)        #imprimir el texto en vertical
#busqueda
print(msg.count("i"))  #numero de "i"
print(msg.find("("))   #lugar del primer "("
print(msg.index("c")) #lugar del primer "c"
