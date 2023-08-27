#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocales in vocales: 
    veces = 0
    for letter in palabra: 
        if letter == vocales:
            veces += 1
    print("La vocal " + vocales + " aparece " + str(veces) + " veces")
