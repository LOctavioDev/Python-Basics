#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

lista = input('INGRESA LA LISTA DE PRODUCTOS SEPARADOS POR UNA COMA (","): ')

print(lista.replace(',', "\n"))