#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "Octavio"
password_prueba = input('INGRESE NUEVAMENTE LA PASSWORD: ')

if password.lower() == password_prueba.lower():
    print('COINCIDEN LAS PASSWORD')
else:
    print('NO COINCIDEN LAS PASSWORD')