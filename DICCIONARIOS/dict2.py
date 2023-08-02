#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

datos = {}

nombre = input('INGRESA TU NOMBRE: ')
edad = input('INGRESA TU EDAD: ')
direccion = input('INGEESA TU DIRECCION: ')
telefono = input('INGRESA TU TELEFONO: ')

datos.update([('Nombre',nombre),('Edad',edad),('Direccion',direccion),('Telefono',telefono)])

print(datos['Nombre'], 'TIENE', datos['Edad'], 'VIVE EN',datos['Direccion'],'Y SU NUMERO DE TELEFO  NO ES',datos['Telefono'])