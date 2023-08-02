#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

#UTILICE EL OPERADOR slicing

frase = input('INGRESA UNA FRASE: ')
print('EL INVERSO DE LA FRASE ES: ' + frase[::-1]) # TOMA LA CADENA QUE ESTA EN LA VARIABLE FRASE Y LOS ":" INDICAN QUE SE SELECCIONARA UNA SUBCADENA COMPLETA Y EL "-1" INDICA QUE LOS ELEMENTOS SE SELECCIONARAN EN ORDEN INVERSO