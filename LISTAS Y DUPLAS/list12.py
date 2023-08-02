vectora = [1,2,3,],[4,5,6]
vectorb = [-1,-0],[0,1],[1,1]

resultado = [[0,0],[0,0]] 

for i in range(len(vectora)):
    for j in range(len(vectorb[0])):
        for k in range(len(vectorb)):
            resultado[i][j] += vectora[i][k] *vectorb[k][j]
for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])
    
    