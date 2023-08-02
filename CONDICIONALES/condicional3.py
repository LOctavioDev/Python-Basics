#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = float(input('INGRESE UN NUMERO: '))
num2 = float(input('INGRESE UN SEGUNDO NUMERO: '))

if num2 == 0 or num1 == 0:
    print('ERROR!!!')
    
else:
    print(num1/num2)