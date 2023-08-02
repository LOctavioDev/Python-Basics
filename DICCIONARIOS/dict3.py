#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {
    'Platano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.80,
    'Naranja': 0.70
}


fruta_elejida = input('INGRESA LA FRUTA QUE QUIERAS: ').title()
kilos = float(input('INGRESA LA CANTIDAD DE KILOS QUE REQUIERES: '))

if fruta_elejida in frutas:
    print(kilos, 'KILOS DE', fruta_elejida, 'CUESTAN', frutas[fruta_elejida]*kilos, '$')

else:
    print('NO HAY EN EXISTENCIA LA FRUTA',fruta_elejida)
    
