#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

print(mcd(48,60))
