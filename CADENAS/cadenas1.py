#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input('INGRESA TU NOMBRE COMPLETO: ')

print(nombre.lower()) #TODO EL TEXTO LO VUELE MINUSCULAS
print(nombre.upper()) #TODO EL TEXTO LO VUELE MAYUSCULA
print(nombre.title()) #LAS PRIMERAS LETRAS DE CADA PALABRA LAS VUELVE MAYUSCULAS

print("Prueba de GIT")