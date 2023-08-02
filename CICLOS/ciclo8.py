#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = '123456789q'
password2 = input('INGRESA LA CONTRASENIA: ')

while(password != password2):
    password2 = input('CONTRASENIA INCORRECTA POR FAVOR VUELVA A INTENTARLO: ')
