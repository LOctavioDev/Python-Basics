#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros_list = [1,2,3,4,5,6,7,8,9,10]

for i in range (1,11):
    print(numeros_list[-i], end=", ")