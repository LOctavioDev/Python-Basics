#Suma de Elementos: Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los elementos.

def Calcular_Suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lis1 = [1,2,3,4,5,6,7,8,9,10]

print(Calcular_Suma(lis1))