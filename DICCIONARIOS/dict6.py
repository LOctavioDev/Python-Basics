#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. 

datos_persona = {}
continuar = True

while continuar:
    clave = input('QUE DATO QUIERES INTRODUCIR?')
    valor = input(clave + ':')
    datos_persona[clave] = valor
    print(datos_persona)
    continuar = input('QUIERES AÑADIR MAS INFORMACION? (Si/No) ') == "Si"
    