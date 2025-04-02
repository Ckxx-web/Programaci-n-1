from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self):
        self.opciones = {}

    @abstractmethod
    def mostrar_opciones(self):
        pass

    @abstractmethod
    def ejecutar_opcion(self, opcion):
        pass

class MenuPago(Menu):
    def __init__(self):
        super().__init__()
        self.opciones = {
            "1": ("Pagar con tarjeta", self.pagar_tarjeta),
            "2": ("Pagar con PSE", self.pagar_pse),
            "3": ("Cancelar pago", self.cancelar_pago)
        }
        self.ejecutando = True

    def mostrar_opciones(self):
        print("\n--- Menú de Pago ---")
        for clave, (descripcion, _) in self.opciones.items():
            print(f"{clave}. {descripcion}")

    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion][1]()
        else:
            print("Ingrese una opción válida.")

    def pagar_tarjeta(self):
        try:
            numero_tarjeta = input("Ingrese el número de tarjeta: ")
            print(numero_tarjeta)
            cvv = input("Ingrese el CVV: ")
            print(cvv)
            print("Pago con tarjeta procesado.")
        except ValueError:
            print("Error: Ingrese datos válidos.")

    def pagar_pse(self):
        try:
            banco = input("Ingrese el nombre del banco: ")
            print(banco)
            numero_cuenta = input("Ingrese el número de cuenta: ")
            print(numero_cuenta)
            print("Pago con PSE procesado.")
        except ValueError:
            print("Error: Ingrese datos válidos.")

    def cancelar_pago(self):
        print("Pago cancelado.")
        self.ejecutando = False

    def iniciar(self):
        while self.ejecutando:
            self.mostrar_opciones()
            opcion = input("Seleccione una opción: ")
            print(opcion)
            self.ejecutar_opcion(opcion)

menu_pago = MenuPago()
menu_pago.iniciar()