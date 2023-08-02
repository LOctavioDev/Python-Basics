#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input('INGRESA UNA PALABRA: ')
palabra_en_reverso = palabra

palabra = list(palabra)
palabra_en_reverso = list(palabra_en_reverso)

palabra_en_reverso.reverse()

if palabra == palabra_en_reverso:
    print('ES PALINDROMO')
else:
    print('NO ES PALINDROMO')
