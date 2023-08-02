#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

subjects = ["PROBABILIDAD", "APLICACIONES WEB", "BASE DE DATOS", "INTEGRADORA", "SISTEMAS OPERATIVOS"]
scores = []
for subject in subjects:
    score = input("INGRESA LA TU CALIFICACION EN: " + subject + ": ")
    scores.append(score)
for i in range(len(subjects)):
    print("EN LA MATERIA " + subjects[i] + " HAS SACADO " + scores[i])