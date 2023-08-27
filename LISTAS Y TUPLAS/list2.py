#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

Materias = ['PROBABILIDAD','APLICACIONES WEB','BASE DE DATOS','SISTEMAS OPERATIVOS','INTEGRADORA']

for i in range(len(Materias)):
    print('YO ESTUDIO: ' + Materias[i])