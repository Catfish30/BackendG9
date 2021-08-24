class Vehiculo:
    def __init__(self, marca,modelo,numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def acelerar(self):
        print("El auto esta acelerando 💨")

    def estado(self):
        return f"Marca:{self.marca} \nModelo:{self.modelo} \nRuedas:{self.numero_ruedas}"

class Auto(Vehiculo):
    def __init__(self, sunroof,marca,modelo):
        self.sunroof = sunroof
        super().__init__(marca,modelo,4)
    def estado(self):
        return "Estado de Auto"

objAuto = Auto(True,"Nissan","Alto")

print(objAuto.marca)

print(objAuto.estado())