# Definición de la clase

class Estudiante:
    def __init__(self,nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
        pass
lista_estudiantes = [
Estudiante('Francisco', 16, [1,10,2,9]),
Estudiante('Ana', 17, [2,9,3,8]),
Estudiante('Karina', 18, [3,8,4,7]),
Estudiante('Camilo', 17, [4,6,5,10]),
]

# Método para sumar las notas
def calcular_suma(notas):
    return sum(notas)
def calcula_prom(notas):
    suma = calcular_suma(notas)
    return suma / len(notas)

for estudiante in lista_estudiantes:
    suma_notas = calcular_suma(estudiante.notas)
    promedios = calcula_prom(estudiante.notas)

    print(f'El promedio de {estudiante.nombre} es de {promedios}')