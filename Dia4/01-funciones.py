

from typing import KeysView


def saludar():
    print('Hola!')

saludar()

# Las variables dentro de las funciones solo existen dntro de ellas,(scope)

def saludarPersona(nombre):
    print(f"Hola como estas {nombre}")

saludarPersona('Josefina')

def sin_nombre():
    """Funcion de muestra"""
    print("Yo soy una funcion sin nombre")
sin_nombre()

# las funciones pueden recibir parametros y estos pueden ser opcionales

def registro(nombre,correo=None):
    print("Registrado")

registro('josefina')
registro('josefina','pina21@casa.com')

# Los parametros predertemiadso siempre van al final
def identificacion(nombre,apellido,nacionalidad='Peruano') :
    datos ={'nombre':nombre,'apellido':apellido,'Nacionalidad':nacionalidad}
    print(datos)

identificacion('Michael',"Huamani")

# parametro con * al comienzo es un parametro especial de python que sirve para almacenar n valores

def alumnos(*args):
    print(args)

alumnos('pina','prin','cavi','mani',12,42,24,True,False)

# ?
# !
# *
# todo

def tareas(nombre,*args):
    print("Ok")

tareas('Pian','1','2','3')



def alumnos_notas(*args):
    desaprobado = 0
    aprobo = 0
    for alumnos in args :
        if(alumnos["promedio"] < 11):
            desaprobado += 1
        else:
            aprobo += 1
    print(f"Desaprobados: {desaprobado}")
    print(f"Aprobados: {aprobo}")


alumnos_notas(
    {"nombre":"Raul", "promedio": 17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16}
)

#  keyword arguments => similar a los args con la diferencia que los kwargs usan el nombre del parametro (nombre='pina')
def indeterminada(**kwargs):
    print(kwargs)

indeterminada(perro="Pina",raza="Cocker",nacionalidad="Boliviana")

def variada(*args,**kwargs):
    print(args,kwargs)