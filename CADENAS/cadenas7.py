#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input('INTRODUZCA EL PRECIO DEL PRODUCTO: ')

print(precio[:precio.find('.')] + ' EUROS Y ' + precio[precio.find('.')+1:] + ' CENTIMOS ')