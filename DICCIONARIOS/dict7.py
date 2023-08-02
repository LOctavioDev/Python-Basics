#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

lista_compra = {}
continuar = True
total_compra = 0

while continuar:
    articulo = input('INGRESA EL NOMBRE DEL ARTICULO: ')
    precio = float(input('INGRESA EL PRECIO DEL ARTICULO $: '))
    total_compra += precio
    lista_compra[articulo] = precio
    continuar = input('DESEAS INGRESAR OTRO DATO? Si/No: ') == 'Si'
    
lista_compra['total'] = total_compra

print(lista_compra)