#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input('INGRESE UNA FRASE: ')
vocal = input('INGRESE UNA VOCAL: ')

print(frase.replace(vocal, vocal.upper())) #REEMPLAZAMOS EN LA CADENA DE FRASE LA VOCAL QUE INTRDOCUIMOS POR LA MISMA VOCAL PERO EN MAYUSCULA