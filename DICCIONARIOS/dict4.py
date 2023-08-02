#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
}

fecha = input('Ingresa la fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')

while int(fecha[1]) > 12 or int(fecha[1]) < 1:
    print('POR FAVOR INGRESA UNA FECHA VALIDA')
    fecha = input('Ingresa la fecha en formato dd/mm/aaaa: ')
    fecha = fecha.split('/')

print('ESTAMOS A:',fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
