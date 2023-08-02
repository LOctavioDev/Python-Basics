#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

Numeros_Ganadores = []

for i in range(0,10):
    valores = int(input('INGRESA EL VALOR GANADOR: '))
    Numeros_Ganadores.append(valores)   

Numeros_Ganadores.sort()
print(Numeros_Ganadores)

    