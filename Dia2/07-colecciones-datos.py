# list => listas
# ordenadas y modificables
colores = ['morado','azul','verde','rojo']

otros = ['manzana',13,True,[1,3,5,7]]

print(colores[-1])
print(colores[2:3])
print(colores[2:])

#copia la lista pero en diferente espacio de memoria
colores_2 = colores[:]

colores.append('celeste')

print(colores[3:])

colores.remove('azul')

print(colores)

colores.pop(0)

print(colores)

color = colores.pop(0)

print(color)
print(colores)


nombre = 'michael'
del nombre
# del elimina variables tambien

del colores[0]

print(colores)

print(len(colores))

# Tuplas ese una collecion de datos ordenas pero una vez creada no se puede editar

notas = (10,15,16,20,10)
print(notas[0])
print(len(notas))
print(notas.count(10))

# Diccionarios 
# JSON 
persona = {
    'nombre':'Michael',
    'mascota': 'Pinafiel',
    'edad': 24,
    'hobbies':[{
        'nombre':'dormir',
        'exp':'avanzado'
    },{
        'nombre':'comer',
        'exp':'experto'
    }
    ]
}

print(persona['hobbies'])

persona['nacionalidad'] = 'peruano'

print(persona)

print (persona['hobbies'][0])