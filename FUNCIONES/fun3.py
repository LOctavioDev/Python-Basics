#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decbin (numero):
    n = list(numero)
    n.reverse()
    decimal = 0
    for i in range (len(numero)):
        decimal += int(numero[i]) * 2 ** i
    return decimal

print(decbin('111'))