
class Perro:
    nombre = ''
    color = ''
    habilidades = []
    raza = ''
    edad = 0


    def ladrar():
        print("Guau Guau")
        # self indica que pertenece a la clase y puede usar sus variables
    def indicar_edad(self): #self es parametro de uso interno
        return "La edad es: {}".format(self.edad)

# creando instancia de la clase (instancias es sacar una copia de la plantilla)
# instancia sinonimo de objeto
perro1 = Perro()
perro1.raza = 'Cocker'
perro1.edad = 2
print(perro1.indicar_edad())


perro2 = Perro()
perro2.edad = 8
print(perro2.indicar_edad())