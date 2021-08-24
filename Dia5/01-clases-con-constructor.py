class Persona:
    def __init__(self,nombre,fecha_nacimiento) :
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def saludar(self):
        print(f"Hola {self.nombre}")

    def __str__(self) :
        """Metodo que sirve para que cuando vayamos a llamar a imprimir el objeto,
        se modifique por algo mas entendible"""
        return self.nombre + " Instancia del objeto"

persona1 = Persona("Michael","30-07-1997")
persona2 = Persona("Paola","20-04-2000")

print(persona1.fecha_nacimiento)
persona1.saludar()

print(persona1)