#Duplicados en una Lista: Crea una función que encuentre y muestre los elementos duplicados en una lista.
def Numeros_Duplicados(lista):
    if not lista:
        return None, None
    elementos_duplicados = []
    
    for i in range(len(lista)):
        for j in range(i+ 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in elementos_duplicados:
                elementos_duplicados.append(lista[i])
    
    return elementos_duplicados

lista = [1,1,2,3,4,5,1,4,5,6,5,2,3,4,10]

print(Numeros_Duplicados(lista))