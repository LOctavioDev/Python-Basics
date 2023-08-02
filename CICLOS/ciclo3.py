#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input('INGRESE UN NUMERO ENTERO: '))
cadena = " "
for i in range(numero+1):
    if i % 2 != 0:
        cadena = cadena + str(i) + (" , ")
print(cadena)