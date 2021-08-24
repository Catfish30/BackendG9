class Electrodomestico:
    def __init__(self):
        self.__nombre = ''
        self.__color = ''
        self.__precio = 0
    
    def __setNombre(self,nombre):
        """El setter srive para definir el contenido del atributo de manera mas formal"""
        self.__nombre = nombre
    
    def __getNombre(self):
        """El getter sirve para devolver el valor de un atributo privado"""
        return self.__nombre

    def __deleteNombre(self):
        # """El deleter sirve para eliminar el contenido de un atributo privado"""
         del self.__nombre

    # property

    nombre = property(__getNombre,__setNombre,__deleteNombre)

objElectrodomestico = Electrodomestico()

objElectrodomestico.nombre = "Lavadora" #setter
print(objElectrodomestico.nombre) #getter
# del objElectrodomestico.nombre #deletter