#Promedio de Números: Crea una función que calcule el promedio de una lista de números.

def Calcular_Promedio(lista):
    suma = 0
    promedio = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

lista = [1,2,3,4,5,6,7,8,9,10]    

print(Calcular_Promedio(lista))