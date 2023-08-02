#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num = int(input('INGRESE UN NUMERO: '))

if num % 2 == 0:
    print('ES PAR')
else:
    print('ES IMPAR')