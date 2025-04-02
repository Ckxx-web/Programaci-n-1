#Crear una clase Factura que permita registrar productos y calcular el total de la compra

from abc import ABC, abstractmethod

class Factura(ABC):
    def __init__(self, producto, cantidad, precio, nombre):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.nombre = nombre

    @abstractmethod
    def total_recibo(self):
        pass

class FacturaCliente(Factura): 
    def total_recibo(self):
        return self.cantidad * self.precio

# Solicitar datos al usuario
nombre_producto = input('Clase de producto: ')
print(nombre_producto)
cantidad_productos = int(input('¿Cuántas prendas?: '))
print(cantidad_productos)
valor_productos = int(input('precio: '))
print(valor_productos)
nomb_cliente = input('Datos del cliente:  ')
print(nomb_cliente)

mi_factura = FacturaCliente(nombre_producto, cantidad_productos, valor_productos, nomb_cliente) 
total = mi_factura.total_recibo()
print(f"El total de la compra fue: {total}")

