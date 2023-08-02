#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input('INGRESA UNA PALABRA: ')

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])#Se utiliza la función len() para obtener la longitud de la palabra y se le resta 1 para obtener el índice del último carácter de la palabra.