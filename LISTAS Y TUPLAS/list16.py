#Encontrar el Mayor y Menor: Escribe una función que encuentre el número mayor y el número menor en una lista de números.

def Mayor_Menor(lista):
    
    if not lista:
        return None, None
    
    mayor = menor = lista[0]
    
    for numero in lista:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    
    
    print(f'EL NUMERO MAYOR DE LA LISTA ES: {mayor} Y EL NUMERO MENOR ES: {menor}')
    
lista = [20,2,3,4,5,6,7,8,9,10]

Mayor_Menor(lista)