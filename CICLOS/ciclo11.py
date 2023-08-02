#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

palara = input('INGRESA UNA PALABRA: ')
cadena = ' '
while palara.lower() != 'salir':
    palara = input('INGRESA UNA PALABRA: ')
    cadena = cadena + palara + ' , '
print(cadena)