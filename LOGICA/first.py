def contar_Vocales (palabra):
    total_vocales = 0
    for letra in palabra:
        if letra in "aeiou":
            total_vocales += 1    
    return total_vocales
print(contar_Vocales("octavio"))