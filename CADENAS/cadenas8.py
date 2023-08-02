#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input('INGRESE SU FECHA DE NACIMIENTO EN FORMATO dd/mm/aaaa: ')
print('DIA ' + fecha[:2])
print('MES ' + fecha[3:5])
print('AÑO ' + fecha[6:])