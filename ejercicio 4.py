#Diseñar una clase Usuario para gestionar autenticaciones en un sistema.
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self,usuario):
        self.usuario = usuario

    @abstractmethod
    def verif(self, info):
        pass

class codu(Usuario):
    def __init__(self,usuario, contra):
        super().__init__(usuario)
        self.contra = contra 
        
    def verif(self, info):
        return self.contra == info

nombre = input('su nombre de usuario: ')
print(nombre)
pin = input('su pin: ')
print(pin)
us = codu(nombre, pin)

codigo_ingresado = input('su pin para verificar: ')
print(codigo_ingresado)

if us.verif(codigo_ingresado):
    print(' Ha sido exitosa la autenticación')
else:
    print('Datos invalidos')
