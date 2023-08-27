#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(abecedario)

for i in reversed(range(len(abecedario))):
 
    if (i+1) % 3 == 0:
        del abecedario[i]
print(abecedario)