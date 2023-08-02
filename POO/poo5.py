class Calculadora:
    def __init__(self, n1, n2):
        self.sum = n1 + n2
        self.rest = n1 - n2
        self.mult = n1 * n2
        self.div = n1 / n2
        
operacion = Calculadora(2,10)
print(operacion.mult)

operacion = Calculadora(2,10)
print(operacion.sum)

operacion = Calculadora(2,10)
print(operacion.rest)

operacion = Calculadora(2,10)
print(operacion.div)