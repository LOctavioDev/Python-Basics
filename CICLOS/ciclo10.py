#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

word = input('INGRESE UNA FRASE: ')
letra = input('INGRESE UNA LETRA: ')
veces = 0

for i in range(len(word)):
    if letra == word[i]:
        veces = veces+1
print('LA LETRA "' + str(letra) + '" APARECIO ' + str(veces) + ' VECES')