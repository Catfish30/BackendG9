
class Vehiculo:
    def __init__(self,largo,ancho,cilindrada,enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.cilindrada = cilindrada
        self.enMarcha = enMarcha
# Cuando queremos indicar que un atributo sera privado (no se podra acceder desde afuera) se le pone antes del nombre __
        self.__alarma = True

    def toogle_alarma(self):
        self.__alarma = True if self.__alarma == False else False

    def encender(self, estado=True):
        resultado = self.__verificar_alarma()
        if resultado:
            self.enMarcha = estado
            print("El vehiculo puede andar 🚗🚗")
        else:
            print("El vehiculo intenta ser robado 🚨🚨")

    def __verificar_alarma(self):
        if self.__alarma == True:
            return False
        else:
            return True

objVehiculo = Vehiculo(2.2,1.5,1200)

# print(objVehiculo.alarma)

objVehiculo.toogle_alarma()
objVehiculo.toogle_alarma()
objVehiculo.toogle_alarma()

# print(objVehiculo.encender())

class Persona:
    def __init__(self,nombre,apellido,correo,password) :
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = self.__encriptar_password (password)

    def __encriptar_password(self,password):
        return "asdjklasdjlk"+password+"sdasdhjkasdjh"

objPersona = Persona(nombre="Michael",apellido='Huamani',correo='michael@correo.com',password="123456")

print(objPersona.password)