from statistics import median

def calcular_media(datos):
    suma = 0
    total_frecuencia = 0
    for intervalo, frecuencia in datos:
        suma += (intervalo[0] + intervalo[1]) / 2 * frecuencia
        total_frecuencia += frecuencia
    media = suma / total_frecuencia
    return media

def calcular_mediana(datos):
    valores = []
    for intervalo, frecuencia in datos:
        valor_medio = (intervalo[0] + intervalo[1]) / 2
        valores.extend([valor_medio] * frecuencia)
    mediana = median(valores)
    return mediana

def calcular_moda(datos):
    moda = max(datos, key=lambda x: x[1])
    return (moda[0][0] + moda[0][1]) / 2


datos = [((13, 15), 4), ((15, 17), 9), ((17, 19), 3), ((19, 21), 3), ((21, 23), 1)]
media = calcular_media(datos)
mediana = calcular_mediana(datos)
moda = calcular_moda(datos)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)