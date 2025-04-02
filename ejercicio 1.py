#Desarrollar Crear una clase Empleado que permita calcular el salario de los empleados

from abc import ABC, abstractmethod

class Empleado(ABC):
    
    def __init__(self, nombre, horas_labor, horas_valor):
        self.nombre = nombre
        self.horas_labor = horas_labor
        self.horas_valor =  horas_valor
        
    @abstractmethod
    def mostrar_salario(self):
        pass

class Empleado(Empleado):
    
    def __init__(self, nombre, horas_labor, horas_valor):
        super().__init__(nombre, horas_labor, horas_valor)
    
    def mostrar_salario(self):
        return self.horas_labor * self.horas_valor


empleado1 = Empleado("Pedro", 8, 35)  
print(f"Salario de {empleado1.nombre}: ${empleado1.mostrar_salario()}")

