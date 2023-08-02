#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input('INGRESA TU NOMBRE: ')
n_veces = int(input('INGRESA LAS VECES QUE QUIERES QUE SE VEA TU NOMBRE: '))
print((nombre + "\n") * n_veces)