#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

lista1 = input('INTRODUCE UNA MUESTRA DE NUMEROS SEPARADOS POR COMAS: ')
lista1 = lista1.split(',')

numeros = len(lista1)

for i in range(numeros):
    lista1[i] = int(lista1[i])
lista1 = tuple(lista1)
suma = 0
sumq = 0

for i in lista1:
    suma += 1
    sumq += i**2

promedio = suma/numeros

desvtip = (sumq/numeros-promedio**2)**(1/2)
print('LA MEDIA ES: ', promedio, ', LA DESCVIACION TIPICA ES: ' , desvtip)