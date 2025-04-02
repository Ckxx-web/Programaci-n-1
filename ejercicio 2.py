# Desarrollar una clase Estudiante que permita almacenar y calcular el promedio de las notas de un estudiante
from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_nota(self):
        pass

class Promedio(Estudiante):
    def __init__(self, nombre, notas):
        super().__init__(nombre)
        self.notas = notas

    def calcular_nota(self):
        if not self.notas:
            return 0 
        return sum(self.notas) / len(self.notas)

materia1 = float(input('Su nota de algebra fue: n/'))
materia2 = float(input('Su nota de calculo fue: n/'))
materia3 = float(input('Su nota de fisica fue: n/'))
notas = [materia1, materia2, materia3]

promedio = Promedio("pedro", notas)
nota_final = promedio.calcular_nota()
print(f"El promedio del semestre de{promedio.nombre} es: {nota_final}")