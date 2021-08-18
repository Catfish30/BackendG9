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