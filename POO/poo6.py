#FUNCIONES PARA ATRIBUTOS
class Persona:
    edad = 27
    nombre = 'Haziel'
    
doctor = Persona()
print(doctor.edad)
print('La edad es: ', getattr(doctor,'edad'))