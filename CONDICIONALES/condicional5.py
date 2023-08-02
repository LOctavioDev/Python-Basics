#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

nombre = int(input('INRESE SU EDAD: '))
ingresos = float(input('INGRESE SUS INGRESOS MENSUALES $: '))

if nombre > 16 and ingresos > 1000:
    print('PUEDE TRIBUTAR')
else:
    print('NO PUEDE TRIBUTAR')