#Matriz Identidad: Escribe una función que genere y devuelva una matriz identidad de tamaño n (una matriz cuadrada con unos en la diagonal y ceros en el resto).

def Matriz_Identidad(size):
    matriz_identidad = [[0] * size for _ in range(size)] # EN Python, el guion bajo se usa para indicar que no necesitas el valor de la variable.
    for i in range(size):
        matriz_identidad[i][i] = 1
    return matriz_identidad

size = 16

new_matriz = Matriz_Identidad(size)

for fila in new_matriz:
    print(fila)