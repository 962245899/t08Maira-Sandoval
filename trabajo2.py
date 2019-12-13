#              10       20
#    012345678901234567890123456
msg="EL QUE RIE ULTIMO RIE MEJOR"
#indexacion
print(msg[7]) #impresion de la letra "R"
print(msg[8])  #impresion de la letra "I"
print(msg[9])  #impresion de la letra "E"

#longitud
print(len("RIE"))      #contabiliza el numero de letras de la palabra "RIE"
print(len("MEJOR"))     #contabiliza el numero de letras de la palabra "MEJOR"
#comparacion
print("El" == "el")     #commpara la palabra escrita
#concatenacion
print(msg[0] + msg[1] + msg[22] + msg[23] + msg[24] + msg[25] + msg[26])     #imprimir la palabra "El MEJOR"
#cortado
print(msg[0:10])       #cortar el fragmento"EL QUE RIE!"
print(msg[::-1])      #invertir el texto
#iteracion
for MEJOR in msg:
    print(MEJOR)        #imprimir el texto en vertical
#busqueda
print(msg.count("E")) #numero de "E"
print(msg.find("O"))   #lugar de la  primera "O"
print(msg.index("M")) #lugar del primer "R"
