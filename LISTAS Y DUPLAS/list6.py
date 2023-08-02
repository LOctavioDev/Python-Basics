#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materias = ['PROBABILIDAD','CALCULO','SISTEMAS','BASE DE DATOS','REDES']
calificaciones = []

for i in reversed(range(len(materias))):
    calificacion = float(input('CUANTO SACASTE EN LA ASIGNATURA ' + materias[i] + ': '))
    if calificacion > 7:
        del materias[i]

print('LAS MATERIAS QUE TIENE QUE REPETIR SON: ' + ', '.join(materias))


    
         
    
