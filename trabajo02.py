#              10       20         30       40        50        60         70       80        90        100      110
#    012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
msg="No es que sea muy listo, es que me quedo durante mas tiempo trabajando en los problemas (albert einstein)"
#indexacion
print(msg[20]) #impresion de la letra "s"
print(msg[104])  #impresion del signo ")"
#longitud
print(len("muy"))      #contabiliza el numero de letras de la palabra "muy"
print(len("trabajando"))     #contabiliza el numero de letras de la palabra "trabajando"
#comparacion
print("que" == "que")     #commpara la palabra escrita
#concatenacion
print(msg[46] + msg[3] + msg[9] + msg[35] + msg[36] + msg[19] + msg[55] + msg[61] + msg[22])     #imprimir la palabra "te quiero"
#cortado
print(msg[88:])       #cortar el fragmento"!(albert einstein)!"
print(msg[::-1])      #invertir el texto
#iteracion
for me in msg:
    print(me)        #imprimir el texto en vertical
#busqueda
print(msg.count("o")) #numero de "o"
print(msg.find("m")) #lugar de la  primera "m"
print(msg.index("que")) #lugar del primer "que"
