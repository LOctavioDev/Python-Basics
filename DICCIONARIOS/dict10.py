import random

def fn_numero_aleatorio_rangos(minimo, maximo):
    return random.randint(minimo, maximo)

cantidad_nombres = int(input("INGRESE LA CANTIDAD DE NOMBRES: "))

nombres = []
for i in range(cantidad_nombres):
    nombre = input("Ingrese el nombre #" + str(i+1) + ": ")
    nombres.append(nombre)

# ACA SE GENERA EL SCRIPT DE MYSQL 
script_mysql = 'SET v_nombre_generado = ELT(fn_numero_aleatorio_rangos(1,{}),\n'.format(cantidad_nombres)
for i in range(cantidad_nombres):
    script_mysql += '                "{}"'.format(nombres[i])
    if i != cantidad_nombres - 1:
        script_mysql += ','
    script_mysql += '\n'
script_mysql += ');'

# LISTO MAMIS
print("EL SCRIPT ES:\n")
print(script_mysql)
