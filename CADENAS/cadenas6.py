#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input('INGRESE SU CORREO ELECTRONICO: ')

print(correo[:correo.find('@')] + '@ceu.es') #ENCUENTRA LA POSICION DEL CARACTER "@" DE LA CADENA "correo" Y DESPUES UTILIZAMOS EL OPERADOR slicing PARA SELECCIONAR DE LA cadena "correo" hasta la posicion del "@" Y DESPUES LO MOSTRAMOS JUNTO CON EL "@ceu.es"  